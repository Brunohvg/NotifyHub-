from django.urls import path
from .views import *

app_name = "pedido_app"

urlpatterns = [
    path("", Pedido.as_view(), name="pedido"),
]
