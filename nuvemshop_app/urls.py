from django.urls import path
from .views import *

app_name = "nuvemshop_app"

urlpatterns = [
    path("", integracao, name="integracao"),
]
