from django.shortcuts import render
from django.views.generic import View, ListView
from django.http import HttpResponse


class Pedido(View):
    def get(self, request):
        # Lógica para lidar com solicitações GET

        return render(request, template_name=("pages/index.html"))
