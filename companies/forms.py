from django import forms
from django.contrib.auth import get_user_model

from companies.models import Company, Recruiter

User = get_user_model()


class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name',)


class RecruiterCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class RecruiterUpdateForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        fields = '__all__'
