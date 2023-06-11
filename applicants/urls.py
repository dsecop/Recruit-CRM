from django.urls import path
from applicants.views import ApplicantListView, ApplicantCreateView, ApplicantDetailView, ApplicantUpdateView

app_name = 'applicants'

urlpatterns = [
    path('', ApplicantListView.as_view(), name='applicant-list'),
    path('create/', ApplicantCreateView.as_view(), name='applicant-create'),
    path('<int:pk>/', ApplicantDetailView.as_view(), name='applicant-detail'),
    path('<int:pk>/update/', ApplicantUpdateView.as_view(), name='applicant-update'),
]
