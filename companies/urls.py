from django.urls import path
from companies.views import CompanyCreateView

app_name = 'companies'

urlpatterns = [
    path('create/', CompanyCreateView.as_view(), name='company-create'),
]
