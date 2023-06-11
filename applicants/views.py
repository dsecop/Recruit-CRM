from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from applicants.forms import ApplicantCreateForm
from applicants.models import Applicant


class ApplicantListView(LoginRequiredMixin, generic.ListView):
    queryset = Applicant.objects.all()
    template_name = 'applicant_list.html'
    context_object_name = 'applicants'


class ApplicantCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = ApplicantCreateForm
    template_name = 'applicant_create.html'
    success_url = reverse_lazy('applicants:applicant-list')

    def form_valid(self, form):
        form.instance.recruiter = self.request.user
        form.instance.company = self.request.user.company
        return super().form_valid(form)
