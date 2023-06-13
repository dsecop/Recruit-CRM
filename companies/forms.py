from django import forms
from django.contrib.auth import get_user_model

from companies.models import Company

User = get_user_model()


class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name',)


class RecruiterCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
