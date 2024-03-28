from django.shortcuts import render, redirect
from libs.nuvemshop import NuvemShop

from django.urls import reverse_lazy

from django.views.generic import CreateView
from .models import LojaIntegrada

nuvemshop = NuvemShop()
PARAMETRO_CODE = "code"


def integracao(request):
    """
    Autentica a loja NuvemShop e cria uma nova instância de integração ou atualiza uma existente.
    """
    # Verifique se o parâmetro 'code' existe na URL
    code = request.GET.get(PARAMETRO_CODE, None)
    lojas = LojaIntegrada.objects.all()

    print(lojas)
    if code is not None:
        return autorizar(request, code=code)  # Chamando a função autorizar
    else:
        return render(request, "nuvemshop_app/integracao.html", {"nova_loja": lojas})


def autorizar(request, code):
    """
    Função para autorizar a loja NuvemShop.
    """
    autorizado = nuvemshop.auth_nuvem_shop(code=code)
    # Faça o que for necessário com a variável 'autorizado'
    access_token = autorizado["access_token"]
    user_id = autorizado["user_id"]
    if access_token and user_id is not None:
        return loja_integrada(request, access_token, user_id)

    return render(request, "nuvemshop_app/integracao.html", {"autorizado": autorizado})


def loja_integrada(request, acess_token, user_id):
    lj_integrada = nuvemshop.store_nuvem(code=acess_token, store_id=user_id)
    id = lj_integrada.get("id")

    if id:
        # Verificar se a loja já existe no banco de dados
        if LojaIntegrada.objects.filter(id=id).exists():
            # Se a loja já existe, buscar a instância existente e renderizar o template
            loja_existente = LojaIntegrada.objects.get(id=id)
            return render(
                request,
                "nuvemshop_app/integracao.html",
                {"lj_integrada": lj_integrada, "loja_existente": loja_existente},
            )

        else:
            # Se a loja não existe, criar uma nova instância no banco de dados
            nova_loja = LojaIntegrada.objects.create(
                id=id,
                nome=lj_integrada["nome"],
                whatsapp_phone_number=lj_integrada["whatsapp_phone_number"],
                contact_email=lj_integrada["contact_email"],
                email=lj_integrada["email"],
                doc=lj_integrada["doc"],
                autorization_token=acess_token,
            )
            return render(
                request,
                "nuvemshop_app/integracao.html",
                {"lj_integrada": lj_integrada, "nova_loja": nova_loja},
            )

    else:
        # Se não há ID, lidar com isso de acordo com a lógica do seu aplicativo
        return render(
            request, "nuvemshop_app/integracao.html", {"lj_integrada": lj_integrada}
        )
