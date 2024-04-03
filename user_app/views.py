from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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


def deslogar(request):
    logout(request)
    return redirect("user_app:authenticacao")
