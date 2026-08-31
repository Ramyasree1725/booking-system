"""Django forms for bookings."""
from __future__ import annotations

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

class BookingsFilterForm(forms.Form):
    """Form: BookingsFilterForm."""
    q = forms.CharField(required=False, max_length=200)
    status = forms.CharField(required=False, max_length=40)
    start = forms.DateTimeField(required=False)
    end = forms.DateTimeField(required=False)
    page = forms.IntegerField(required=False, min_value=1, initial=1)
    page_size = forms.IntegerField(required=False, min_value=1, max_value=200, initial=20)

    def clean(self):
        cleaned = super().clean()
        start, end = cleaned.get("start"), cleaned.get("end")
        if start and end and end < start:
            raise ValidationError("end must be after start")
        return cleaned

    def clean_q(self):
        q = self.cleaned_data.get("q") or ""
        return q.strip()[:200]

class BookingsCreateForm(forms.Form):
    """Form: BookingsCreateForm."""
    q = forms.CharField(required=False, max_length=200)
    status = forms.CharField(required=False, max_length=40)
    start = forms.DateTimeField(required=False)
    end = forms.DateTimeField(required=False)
    page = forms.IntegerField(required=False, min_value=1, initial=1)
    page_size = forms.IntegerField(required=False, min_value=1, max_value=200, initial=20)

    def clean(self):
        cleaned = super().clean()
        start, end = cleaned.get("start"), cleaned.get("end")
        if start and end and end < start:
            raise ValidationError("end must be after start")
        return cleaned

    def clean_q(self):
        q = self.cleaned_data.get("q") or ""
        return q.strip()[:200]

class BookingsUpdateForm(forms.Form):
    """Form: BookingsUpdateForm."""
    q = forms.CharField(required=False, max_length=200)
    status = forms.CharField(required=False, max_length=40)
    start = forms.DateTimeField(required=False)
    end = forms.DateTimeField(required=False)
    page = forms.IntegerField(required=False, min_value=1, initial=1)
    page_size = forms.IntegerField(required=False, min_value=1, max_value=200, initial=20)

    def clean(self):
        cleaned = super().clean()
        start, end = cleaned.get("start"), cleaned.get("end")
        if start and end and end < start:
            raise ValidationError("end must be after start")
        return cleaned

    def clean_q(self):
        q = self.cleaned_data.get("q") or ""
        return q.strip()[:200]

class BookingsSearchForm(forms.Form):
    """Form: BookingsSearchForm."""
    q = forms.CharField(required=False, max_length=200)
    status = forms.CharField(required=False, max_length=40)
    start = forms.DateTimeField(required=False)
    end = forms.DateTimeField(required=False)
    page = forms.IntegerField(required=False, min_value=1, initial=1)
    page_size = forms.IntegerField(required=False, min_value=1, max_value=200, initial=20)

    def clean(self):
        cleaned = super().clean()
        start, end = cleaned.get("start"), cleaned.get("end")
        if start and end and end < start:
            raise ValidationError("end must be after start")
        return cleaned

    def clean_q(self):
        q = self.cleaned_data.get("q") or ""
        return q.strip()[:200]

class BookingsExportForm(forms.Form):
    """Form: BookingsExportForm."""
    q = forms.CharField(required=False, max_length=200)
    status = forms.CharField(required=False, max_length=40)
    start = forms.DateTimeField(required=False)
    end = forms.DateTimeField(required=False)
    page = forms.IntegerField(required=False, min_value=1, initial=1)
    page_size = forms.IntegerField(required=False, min_value=1, max_value=200, initial=20)

    def clean(self):
        cleaned = super().clean()
        start, end = cleaned.get("start"), cleaned.get("end")
        if start and end and end < start:
            raise ValidationError("end must be after start")
        return cleaned

    def clean_q(self):
        q = self.cleaned_data.get("q") or ""
        return q.strip()[:200]

class BookingsBulkActionForm(forms.Form):
    """Form: BookingsBulkActionForm."""
    q = forms.CharField(required=False, max_length=200)
    status = forms.CharField(required=False, max_length=40)
    start = forms.DateTimeField(required=False)
    end = forms.DateTimeField(required=False)
    page = forms.IntegerField(required=False, min_value=1, initial=1)
    page_size = forms.IntegerField(required=False, min_value=1, max_value=200, initial=20)

    def clean(self):
        cleaned = super().clean()
        start, end = cleaned.get("start"), cleaned.get("end")
        if start and end and end < start:
            raise ValidationError("end must be after start")
        return cleaned

    def clean_q(self):
        q = self.cleaned_data.get("q") or ""
        return q.strip()[:200]

class BookingsExtraForm0(forms.Form):
    """Extra form variant 0 for bookings."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class BookingsExtraForm1(forms.Form):
    """Extra form variant 1 for bookings."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class BookingsExtraForm2(forms.Form):
    """Extra form variant 2 for bookings."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class BookingsExtraForm3(forms.Form):
    """Extra form variant 3 for bookings."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class BookingsExtraForm4(forms.Form):
    """Extra form variant 4 for bookings."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class BookingsExtraForm5(forms.Form):
    """Extra form variant 5 for bookings."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class BookingsExtraForm6(forms.Form):
    """Extra form variant 6 for bookings."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class BookingsExtraForm7(forms.Form):
    """Extra form variant 7 for bookings."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class BookingsExtraForm8(forms.Form):
    """Extra form variant 8 for bookings."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class BookingsExtraForm9(forms.Form):
    """Extra form variant 9 for bookings."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()
