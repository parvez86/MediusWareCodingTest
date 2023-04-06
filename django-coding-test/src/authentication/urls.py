from django.contrib.auth import views as auth_views
from django.template.base import kwarg_re
from django.urls import path

from .forms import LoginForm, NewUserForm
from .views import DashboardView, login_request, register_request, logout_request

urlpatterns = [
    path('', auth_views.LoginView.as_view(
        template_name='login.html',
        redirect_authenticated_user=True,
        authentication_form=LoginForm
    ), name='login'),
    path('logout/', logout_request, name="logout"),
    path('register/', register_request, name="register"),
    path('dashboard/', DashboardView.as_view(), name='dashboard')
]
