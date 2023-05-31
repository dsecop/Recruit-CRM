from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_applicant = models.BooleanField(default=False)
    is_recruiter = models.BooleanField(default=True)
    email = models.EmailField(unique=True, max_length=120, verbose_name='email address')
