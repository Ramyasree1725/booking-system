"""Django forms for reporting."""
from __future__ import annotations

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

class ReportingFilterForm(forms.Form):
    """Form: ReportingFilterForm."""
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

class ReportingCreateForm(forms.Form):
    """Form: ReportingCreateForm."""
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

class ReportingUpdateForm(forms.Form):
    """Form: ReportingUpdateForm."""
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

class ReportingSearchForm(forms.Form):
    """Form: ReportingSearchForm."""
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

class ReportingExportForm(forms.Form):
    """Form: ReportingExportForm."""
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

class ReportingBulkActionForm(forms.Form):
    """Form: ReportingBulkActionForm."""
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

class ReportingExtraForm0(forms.Form):
    """Extra form variant 0 for reporting."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class ReportingExtraForm1(forms.Form):
    """Extra form variant 1 for reporting."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class ReportingExtraForm2(forms.Form):
    """Extra form variant 2 for reporting."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class ReportingExtraForm3(forms.Form):
    """Extra form variant 3 for reporting."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class ReportingExtraForm4(forms.Form):
    """Extra form variant 4 for reporting."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class ReportingExtraForm5(forms.Form):
    """Extra form variant 5 for reporting."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class ReportingExtraForm6(forms.Form):
    """Extra form variant 6 for reporting."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class ReportingExtraForm7(forms.Form):
    """Extra form variant 7 for reporting."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class ReportingExtraForm8(forms.Form):
    """Extra form variant 8 for reporting."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class ReportingExtraForm9(forms.Form):
    """Extra form variant 9 for reporting."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()
