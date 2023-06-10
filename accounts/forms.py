from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'email', 'is_company_owner', 'is_recruiter')
        labels = {
            'is_company_owner': 'Register as a company',
            'is_recruiter': 'Register as a recruiter',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_description in ('username', 'password1', 'password2'):
            self.fields[field_description].help_text = ''


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'email', 'is_company_owner', 'is_recruiter')
