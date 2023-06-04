from django.db import models

from accounts.models import CustomUser
from tags.models import Tag
from companies.models import Company


class Applicant(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    title = models.CharField(max_length=30, blank=True)
    note = models.TextField(max_length=200, blank=True)
    city = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True, max_length=120, verbose_name='email address')
    tags = models.ManyToManyField(Tag, blank=True)
    profile_picture = models.ImageField(blank=True, null=True, upload_to='profile_pictures/')
    recruiter = models.ForeignKey(CustomUser, related_name='applicants', null=True, blank=True, on_delete=models.SET_NULL)
    company = models.ForeignKey(Company, related_name='applicants', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
