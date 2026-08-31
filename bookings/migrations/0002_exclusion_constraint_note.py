# Placeholder migration documenting the PostgreSQL ExclusionConstraint.
# When running on PostgreSQL, replace this with a real RunSQL / AddConstraint
# using tstzrange for race-condition-safe double-booking prevention.
#
# Example (PostgreSQL only):
#
# from django.contrib.postgres.constraints import ExclusionConstraint
# from django.contrib.postgres.fields import RangeOperators
# from django.db.models import Q
# from django.contrib.postgres.fields.ranges import DateTimeRangeField
#
# operations = [
#     migrations.AddConstraint(
#         model_name='booking',
#         constraint=ExclusionConstraint(
#             name='prevent_overlapping_bookings',
#             expressions=[
#                 ('resource', RangeOperators.EQUAL),
#                 (DateTimeRangeField('start_datetime', 'end_datetime'), RangeOperators.OVERLAPS),
#             ],
#             condition=Q(status__in=['confirmed', 'pending']),
#         ),
#     ),
# ]

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = []  # will be fixed after first makemigrations
    operations = []
