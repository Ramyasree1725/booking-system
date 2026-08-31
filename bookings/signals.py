from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Booking, BookingNotification


@receiver(post_save, sender=Booking)
def booking_notification_handler(sender, instance, created, **kwargs):
    if created:
        ntype = BookingNotification.NotificationType.CREATED
        if instance.status == Booking.Status.PENDING:
            ntype = BookingNotification.NotificationType.APPROVAL_NEEDED
        _send_notification(instance, ntype, instance.user)
    else:
        if instance.status == Booking.Status.CANCELLED:
            _send_notification(instance, BookingNotification.NotificationType.CANCELLED, instance.user)
        elif instance.status == Booking.Status.CONFIRMED and instance.approved_at:
            _send_notification(instance, BookingNotification.NotificationType.CONFIRMED, instance.user)


def _send_notification(booking, ntype, recipient):
    if not recipient.notification_email:
        return
    notif = BookingNotification.objects.create(
        booking=booking,
        notification_type=ntype,
        recipient=recipient,
    )
    subject = f'[Booking] {ntype.label}: {booking.title}'
    message = (
        f'Booking: {booking.title}\n'
        f'Resource: {booking.resource.name}\n'
        f'When: {booking.start_datetime:%Y-%m-%d %H:%M} – {booking.end_datetime:%H:%M}\n'
        f'Status: {booking.get_status_display()}\n'
    )
    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [recipient.email],
            fail_silently=False,
        )
        notif.is_sent = True
        notif.sent_at = timezone_now()
        notif.save(update_fields=['is_sent', 'sent_at'])
    except Exception as e:
        notif.error_message = str(e)
        notif.save(update_fields=['error_message'])


def timezone_now():
    from django.utils import timezone
    return timezone.now()
