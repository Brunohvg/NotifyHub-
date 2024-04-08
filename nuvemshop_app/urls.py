from django.urls import path
from .views import *


app_name = "nuvemshop_app"

urlpatterns = [
    path("integracao", integracao, name="integracao"),
    path("get_clientes", integracao, name="get_clientes"),
]
