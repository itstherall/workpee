from math import prod
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from login.forms import NewUserForm, PedidoForm, PedidoFormSet, ProdutoForm, ProdutoFormSet

from login.models import Loja, Produto

# Create your views here.


def index(request):
    produto = Produto.objects.all()

    if request.user.is_authenticated:
        usuario = request.user
    else:
        usuario = ''
    return render(request, 'workpee/index.html', {'usuario': usuario, 'produtos': produto})


def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            loja = Loja(nome=user.username, descricao="")
            loja.save()
            print(loja)
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


def perfil(request, id):

    loja = Loja.objects.get(id=id)

    produtos = Produto.objects.filter(loja=id)
    print(produtos)
    if request.user.is_authenticated:
        usuario = request.user
    else:
        usuario = 'João'
    return render(request, 'workpee/perfil.html', {'produtos': produtos, 'usuario': usuario, 'loja': loja})


def produto(request, id):
    produto = Produto.objects.get(id=id)
    form = PedidoFormSet()
    user = request.user

    if request.method == "POST":
        form = PedidoFormSet(request.POST, instance=produto)
        if form.is_valid():
            form.save()

    return render(request, 'workpee/produto.html', {'produto': produto, "form": form, "user": user})


def add_produto(request):

    loja = Loja.objects.get(id=request.user.id)
    form = ProdutoFormSet()

    if request.method == 'POST':
        form = ProdutoFormSet(request.POST, request.FILES, instance=loja)
        if form.is_valid():
            print(form.is_valid())
            form.save()
            return redirect('acc:perfil', loja.id)

    return render(request, 'workpee/add_produto.html', {'form': form})
