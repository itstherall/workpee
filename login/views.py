from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from login.forms import NewUserForm

from login.models import Produto

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        usuario = request.user
    else:
        usuario = ''
    return render(request, 'workpee/index.html', {'usuario': usuario})


def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("acc:home")
        else:
            messages.error(
                request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewUserForm()
        return render(request=request, template_name="signup.html", context={"register_form": form})


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
                return redirect("acc:home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form": form})


def perfil(request):
    produtos = Produto.objects.all()
    return render(request, 'workpee/perfil.html', {'produtos': produtos})
