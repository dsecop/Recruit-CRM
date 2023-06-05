from django.urls import path
from applicants.views import ApplicantListView, ApplicantCreateView

app_name = 'applicants'

urlpatterns = [
    path('', ApplicantListView.as_view(), name='applicant-list'),
    path('create/', ApplicantCreateView.as_view(), name='applicant-create'),
]
