from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.
from django import views
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

from .forms import LoginForm, NewUserForm


@csrf_protect
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = LoginForm()
    context = {"login_form": form}
    print(context)
    return render(request=request, template_name="login.html", context=context)


@csrf_protect
def register_request(request):
    if request.method == "POST":
        print(request.POST)
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Registration successful. {form}")
            login(request, user)
            print("user creation successfully")
            return redirect("dashboard")
        messages.error(request, "Unsuccessful login. Invalid information.")
        print("user creation failed")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


@login_required
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login")


@method_decorator(login_required, name='dispatch')
class DashboardView(views.generic.TemplateView):
    template_name = 'dashboard.html'
