from django.urls import path
from . import views


app_name = "nuvemshop_app"

urlpatterns = [
    path("integracao", views.integracao, name="integracao"),
    path("", views.desativar_integracao, name="desativar_integracao"),
]
