from django import forms
from companies.models import Company


class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name',)
