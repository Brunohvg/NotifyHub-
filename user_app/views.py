from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.http import require_POST

from django.contrib.auth.signals import user_logged_out
from django.core.cache import cache


# Create your views here.
def authenticacao(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect("nuvemshop_app:integracao")
        messages.success(
            request,
            "Usuario ou senha invalido",
        )

    return render(request, "user_app/login.html")


def cadastrar_usuario(request):
    if request.method == "GET":
        return render(request, "user_app/registrar.html")
    try:
        usuario_aux = User.objects.get(email=request.POST["email"])

        if usuario_aux:

            return render(
                request,
                "user_app/login.html",
                messages.error(request, "Já existe um usuário com o mesmo e-mail"),
            )

    except User.DoesNotExist:
        nome_usuario = request.POST["nome"]
        email = request.POST["email"]
        senha = request.POST["password"]

        novoUsuario = User.objects.create_user(
            username=nome_usuario, email=email, password=senha
        )
        novoUsuario.save()
        return redirect("nuvemshop_app:integracao")


def deslogar(request):
    logout(request)
    return redirect("user_app:authenticacao")
