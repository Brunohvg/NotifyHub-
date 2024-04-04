from django.urls import path
from . import views


app_name = "user_app"

urlpatterns = [
    path("", views.authenticacao, name="authenticacao"),
    path("deslogar/", views.deslogar, name="deslogar"),
    path("registrar/", views.cadastrar_usuario, name="registrar"),
]
