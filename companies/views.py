from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from companies.forms import CompanyCreateForm
from companies.models import Company
from companies.models import Recruiter


class CompanyCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = CompanyCreateForm
    template_name = 'company_create.html'
    success_url = reverse_lazy('applicants:applicant-list')

    def dispatch(self, request, *args, **kwargs):
        if Company.objects.filter(owner=self.request.user.id):
            return redirect('applicants:applicant-list')
        return super().dispatch(request, *args, **kwargs)

    @transaction.atomic
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class RecruiterListView(LoginRequiredMixin, generic.ListView):
    template_name = 'recruiter_list.html'
    context_object_name = 'recruiters'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_company_owner:
            return redirect('applicants:applicant-list')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        company = user.company
        return Recruiter.objects.filter(company=company)
