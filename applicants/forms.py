from django import forms
from applicants.models import Applicant


class ApplicantCreateForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ('first_name', 'last_name', 'email')


class ApplicantUpdateForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ('first_name',
                  'last_name',
                  'email',
                  'title',
                  'city',
                  'profile_picture',
                  'note',
                  )
