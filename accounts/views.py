from django.db import transaction
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
        to_return = super().form_valid(form)
        user = form.save()
        if user.is_company_owner:
            Company.objects.create(name='default', owner=user)
            user.save()
        return to_return


class HomePageView(generic.TemplateView):
    template_name = 'home_page.html'
