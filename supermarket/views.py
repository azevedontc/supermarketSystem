from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, UpdateView, ListView
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.urls import reverse

from .models import User, Caixas, Product
from .forms import Login_form, Register_form

# Create your views here.
def index(request):
    context = {"caixas": Caixas.objects.all()}
    return render(request, "core/index.html", context)


def call_staff(request):
    ''' chama um funcionario até o local do cliente '''
    return render(request, "core/staff.html")


def frios(request):
    ''' Página de serviço especial de itens frios'''
    context = {"caixas": Caixas.objects.filter(option="frios")}
    return render(request, "core/frios.html", context)


def entrega(request):
    ''' Página de serviço especial de entrega'''
    context = {"caixas": Caixas.objects.filter(option="entrega")}
    return render(request, "core/entrega.html", context)


def presente(request):
    ''' Página de serviço especial de itens presente'''
    context = {"caixas": Caixas.objects.filter(option="presente")}
    return render(request, "core/presente.html", context)


def promotions(request):
    ''' Lista todos os produtos em promoção '''
    return render(request, "core/presente.html")


def search(request):
    ''' search view '''
    search = request.GET['q']
    results = Product.objects.filter(name__contains=search)

    context = {
        "results": results,
        "search": search
    }

    return render(request, "core/search.html", context)


def volumes(request):
    ''' Página de serviço especial de itens volumes'''
    return render(request, "core/volumes.html")


def logout_view(request):
    ''' Desconecta o usuario '''
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def login_view(request):
    ''' Acessar uma conta '''
    context = {"form": Login_form()}

    if request.method == "POST":
        form = Login_form(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            # Check if authentication successful
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                context["error"] = "Invalid username and/or password."
                return render(request, "core/login.html", context)

    return render(request, "core/login.html", context)


class Register(CreateView):
    ''' Cria uma nova conta '''
    model = User
    form_class = Register_form
    template_name = "core/register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(reverse("index"))


def delete_account(request):
    ''' Exclui a conta do úsuario quando solicitado '''
    user = User.objects.get(username=request.user.username)
    user.delete()
    return HttpResponseRedirect(reverse("login"))