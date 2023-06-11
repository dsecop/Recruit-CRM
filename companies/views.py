from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from companies.forms import CompanyCreateForm
from companies.models import Company


class CompanyCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = CompanyCreateForm
    template_name = 'company_create.html'
    success_url = reverse_lazy('applicants:applicant-list')

    def dispatch(self, request, *args, **kwargs):
        if Company.objects.filter(owner=self.request.user):
            return redirect('applicants:applicant-list')
        return super().dispatch(request, *args, **kwargs)

    @transaction.atomic
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
