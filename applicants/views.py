from django.views import generic

from applicants.models import Applicant


class ApplicantListView(generic.ListView):
    queryset = Applicant.objects.all()
    template_name = 'applicant_list.html'
    context_object_name = 'applicants'
