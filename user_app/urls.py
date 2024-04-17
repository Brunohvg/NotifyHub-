from django.urls import path
from . import views


app_name = "user_app"

urlpatterns = [
    path("login", views.authenticacao, name="authenticacao"),
    path("deslogar", views.deslogar, name="deslogar"),
    path("registre-se", views.cadastrar_usuario, name="registrar"),
    path("perfil", views.perfil, name="perfil"),
]
