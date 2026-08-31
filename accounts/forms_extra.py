"""Django forms for accounts."""
from __future__ import annotations

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

class AccountsFilterForm(forms.Form):
    """Form: AccountsFilterForm."""
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

class AccountsCreateForm(forms.Form):
    """Form: AccountsCreateForm."""
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

class AccountsUpdateForm(forms.Form):
    """Form: AccountsUpdateForm."""
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

class AccountsSearchForm(forms.Form):
    """Form: AccountsSearchForm."""
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

class AccountsExportForm(forms.Form):
    """Form: AccountsExportForm."""
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

class AccountsBulkActionForm(forms.Form):
    """Form: AccountsBulkActionForm."""
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

class AccountsExtraForm0(forms.Form):
    """Extra form variant 0 for accounts."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class AccountsExtraForm1(forms.Form):
    """Extra form variant 1 for accounts."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class AccountsExtraForm2(forms.Form):
    """Extra form variant 2 for accounts."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class AccountsExtraForm3(forms.Form):
    """Extra form variant 3 for accounts."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class AccountsExtraForm4(forms.Form):
    """Extra form variant 4 for accounts."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class AccountsExtraForm5(forms.Form):
    """Extra form variant 5 for accounts."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class AccountsExtraForm6(forms.Form):
    """Extra form variant 6 for accounts."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class AccountsExtraForm7(forms.Form):
    """Extra form variant 7 for accounts."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class AccountsExtraForm8(forms.Form):
    """Extra form variant 8 for accounts."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()

class AccountsExtraForm9(forms.Form):
    """Extra form variant 9 for accounts."""
    field_a = forms.CharField(required=False, max_length=100)
    field_b = forms.IntegerField(required=False, min_value=0)
    field_c = forms.BooleanField(required=False)
    field_d = forms.DateField(required=False)
    field_e = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    def clean_field_a(self):
        val = self.cleaned_data.get("field_a") or ""
        return val.strip()
