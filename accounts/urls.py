from django.urls import path
from django.contrib.auth import views as auth_view
from accounts.views import SignUpView

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
