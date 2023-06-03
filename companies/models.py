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


class Recruiter(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.email}'
