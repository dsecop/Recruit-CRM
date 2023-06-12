from django.urls import path
from companies.views import (
    CompanyCreateView,
    RecruiterListView,
)

app_name = 'companies'

urlpatterns = [
    path('', RecruiterListView.as_view(), name='recruiter-list'),
    path('create/', CompanyCreateView.as_view(), name='company-create'),
]
