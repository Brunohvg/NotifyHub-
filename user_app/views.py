from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


from django.contrib.auth.signals import user_logged_out
from django.core.cache import cache


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        messages.success(request, {username})
        print(username, password)

    return render(request, "user_app/login.html")
