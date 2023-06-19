from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class CompanyOwnerMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_company_owner:
            return redirect('applicants:applicant-list')
        return super().dispatch(request, *args, **kwargs)
