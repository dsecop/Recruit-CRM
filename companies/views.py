import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from applicants.models import Applicant
from companies.forms import CompanyCreateForm, RecruiterCreateForm, RecruiterUpdateForm
from companies.mixins import CompanyOwnerMixin
from companies.models import Company
from companies.models import Recruiter


class CompanyCreateView(LoginRequiredMixin, CompanyOwnerMixin, generic.CreateView):
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


class CompanyDashboardView(LoginRequiredMixin, CompanyOwnerMixin, generic.DetailView):
    model = Company
    template_name = 'company_dashboard.html'
    context_object_name = 'company'

    def get_queryset(self):
        company = self.request.user.company
        return Company.objects.filter(owner_id=company.owner_id)

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(CompanyDashboardView, self).get_context_data(**kwargs)
        total_applicant_number = Applicant.objects.filter(company=user.company).count()
        context.update({
            'total_applicant_number': total_applicant_number,
        })
        return context


class RecruiterListView(LoginRequiredMixin, CompanyOwnerMixin, generic.ListView):
    template_name = 'recruiter_list.html'
    context_object_name = 'recruiters'

    def get_queryset(self):
        user = self.request.user
        company = user.company
        return Recruiter.objects.filter(company=company)


class RecruiterCreateView(LoginRequiredMixin, CompanyOwnerMixin, generic.CreateView):
    form_class = RecruiterCreateForm
    template_name = 'recruiter_create.html'
    success_url = reverse_lazy('companies:recruiter-list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_company_owner = False
        user.is_recruiter = True
        user.set_password(f'{random.randint(0, 10000)}')
        user.save()
        Recruiter.objects.create(user=user, company=self.request.user.company)
        return super(RecruiterCreateView, self).form_valid(form)


class RecruiterDetailView(LoginRequiredMixin, CompanyOwnerMixin, generic.DetailView):
    template_name = 'recruiter_detail.html'
    context_object_name = 'recruiter'

    def get_queryset(self):
        user = self.request.user
        company = user.company
        return Recruiter.objects.filter(company=company)


class RecruiterUpdateView(LoginRequiredMixin, CompanyOwnerMixin, generic.UpdateView):
    form_class = RecruiterUpdateForm
    template_name = 'recruiter_update.html'
    success_url = reverse_lazy('companies:recruiter-list')

    def get_queryset(self):
        user = self.request.user
        company = user.company
        return Recruiter.objects.filter(company=company)


class RecruiterDeleteView(LoginRequiredMixin, CompanyOwnerMixin, generic.DeleteView):
    template_name = 'recruiter_delete.html'
    success_url = reverse_lazy('companies:recruiter-list')

    def get_queryset(self):
        user = self.request.user
        company = user.company
        return Recruiter.objects.filter(company=company)
