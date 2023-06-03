from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_company = models.BooleanField(default=True)
    is_recruiter = models.BooleanField(default=False)
    email = models.EmailField(unique=True, max_length=120, verbose_name='email address')
