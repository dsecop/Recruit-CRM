from django.db import models
from accounts.models import CustomUser


class Company(models.Model):
    name = models.CharField(max_length=150)
    website = models.CharField(max_length=200, blank=True, null=True)
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'companies'

    def __str__(self):
        return f'{self.name}'
