"""Django forms for resources."""
from __future__ import annotations

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

class ResourcesFilterForm(forms.Form):
    """Form: ResourcesFilterForm."""
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

class ResourcesCreateForm(forms.Form):
    """Form: ResourcesCreateForm."""
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

class ResourcesUpdateForm(forms.Form):
    """Form: ResourcesUpdateForm."""
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

class ResourcesSearchForm(forms.Form):
    """Form: ResourcesSearchForm."""
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

class ResourcesExportForm(forms.Form):
    """Form: ResourcesExportForm."""
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

class ResourcesBulkActionForm(forms.Form):
    """Form: ResourcesBulkActionForm."""
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

class ResourcesExtraForm0(forms.Form):
    """Extra form variant 0 for resources."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class ResourcesExtraForm1(forms.Form):
    """Extra form variant 1 for resources."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class ResourcesExtraForm2(forms.Form):
    """Extra form variant 2 for resources."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class ResourcesExtraForm3(forms.Form):
    """Extra form variant 3 for resources."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class ResourcesExtraForm4(forms.Form):
    """Extra form variant 4 for resources."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class ResourcesExtraForm5(forms.Form):
    """Extra form variant 5 for resources."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class ResourcesExtraForm6(forms.Form):
    """Extra form variant 6 for resources."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class ResourcesExtraForm7(forms.Form):
    """Extra form variant 7 for resources."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class ResourcesExtraForm8(forms.Form):
    """Extra form variant 8 for resources."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class ResourcesExtraForm9(forms.Form):
    """Extra form variant 9 for resources."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()
