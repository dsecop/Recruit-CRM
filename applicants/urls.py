from django.urls import path
from applicants.views import ApplicantListView

app_name = 'applicants'

urlpatterns = [
    path('', ApplicantListView.as_view(), name='applicant-list'),
]
