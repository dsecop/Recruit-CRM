from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from applicants.forms import ApplicantCreateForm, ApplicantUpdateForm
from applicants.models import Applicant


class ApplicantListView(LoginRequiredMixin, generic.ListView):
    queryset = Applicant.objects.all()
    template_name = 'applicant_list.html'
    context_object_name = 'applicants'

    def get_queryset(self):
        user = self.request.user
        if user.is_company_owner:
            queryset = Applicant.objects.filter(company=user.company)
        else:
            queryset = Applicant.objects.filter(recruiter=user)
        return queryset


class ApplicantCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = ApplicantCreateForm
    template_name = 'applicant_create.html'
    success_url = reverse_lazy('applicants:applicant-list')

    def form_valid(self, form):
        form.instance.recruiter = self.request.user
        form.instance.company = self.request.user.recruiter.company
        return super().form_valid(form)


class ApplicantDetailView(LoginRequiredMixin, generic.DetailView):
    model = Applicant
    template_name = 'applicant_detail.html'
    context_object_name = 'applicant'


class ApplicantUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Applicant
    form_class = ApplicantUpdateForm
    template_name = 'applicant_update.html'
    success_url = reverse_lazy('applicants:applicant-list')

    def get_queryset(self):
        user = self.request.user
        return Applicant.objects.filter(company=user.company)


class ApplicantDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'applicant_delete.html'
    success_url = reverse_lazy('applicants:applicant-list')

    def get_queryset(self):
        user = self.request.user
        return Applicant.objects.filter(company=user.company)
