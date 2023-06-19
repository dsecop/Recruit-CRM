from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import CustomUserCreationForm
from companies.models import Company


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'registration/signup.html'

    @transaction.atomic
    def form_valid(self, form):
        user = form.save()
        if user.is_company_owner:
            Company.objects.create(name='default', owner=user)
        return super(SignUpView, self).form_valid(form)


class HomePageView(generic.TemplateView):
    template_name = 'home_page.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_company_owner:
            return redirect('companies:company-dashboard', pk=self.request.user.company.id)
        return super().dispatch(request, *args, **kwargs)
