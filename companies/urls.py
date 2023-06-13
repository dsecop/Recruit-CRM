from django.urls import path
from companies.views import (
    CompanyCreateView,
    RecruiterListView,
    RecruiterCreateView,
)

app_name = 'companies'

urlpatterns = [
    path('', RecruiterListView.as_view(), name='recruiter-list'),
    path('create/', CompanyCreateView.as_view(), name='company-create'),
    path('create/recruiter/', RecruiterCreateView.as_view(), name='recruiter-create'),
]
