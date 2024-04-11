from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import LojaIntegrada
from libs.nuvemshop import NuvemShop
from django.contrib import messages

nuvemshop = NuvemShop()
PARAMETRO_CODE = "code"


@login_required
def integracao(request):
    """
    Página de integração onde o usuário pode autorizar uma loja NuvemShop.
    """

    code = request.GET.get(PARAMETRO_CODE, None)
    lojas = LojaIntegrada.objects.all()
    if code is not None:
        return autorizar(request, code=code)
    else:
        return render(request, "nuvemshop_app/integracao.html", {"nova_loja": lojas})


@login_required
def autorizar(request, code):
    """
    Função para autorizar a loja NuvemShop.
    """

    autorizado = nuvemshop.auth_nuvem_shop(code=code)
    access_token = autorizado.get("access_token")
    user_id = autorizado.get("user_id")
    id_existe = LojaIntegrada.objects.filter(id=user_id).first()
    if id_existe is not None:
        messages.error(
            request, f"Esta loja já está em uso com outro email {id_existe.email}"
        )
        return redirect("nuvemshop_app:integracao")

    if access_token and user_id:
        return loja_integrada(request, access_token, user_id)

    return render(request, "nuvemshop_app/integracao.html", {"autorizado": autorizado})


"""@login_required
def loja_integrada(request, access_token, user_id):
 
    usuario = request.user
    lj_integrada = nuvemshop.store_nuvem(code=access_token, store_id=user_id)
    id = lj_integrada.get("id")

    loja_existente = LojaIntegrada.objects.filter(id=id, ativa=False).first()

    if loja_existente:
        return messages.error(request, "Está loja já esta em uso com outro email")
    else:
        nova_loja = LojaIntegrada.objects.create(
            id=id,
            nome=lj_integrada.get("nome"),
            whatsapp_phone_number=lj_integrada.get("whatsapp_phone_number"),
            contact_email=lj_integrada.get("contact_email"),
            email=lj_integrada.get("email"),
            doc=lj_integrada.get("doc"),
            autorization_token=access_token,
            usuario=usuario,
        )
        return render(
            request,
            "nuvemshop_app/integracao.html",
            {"lj_integrada": lj_integrada, "nova_loja": nova_loja},
        )
"""


@login_required
def loja_integrada(request, access_token, user_id):
    """
    Função para lidar com a integração de uma loja NuvemShop.
    """
    usuario = request.user
    lj_integrada = nuvemshop.store_nuvem(code=access_token, store_id=user_id)
    id = lj_integrada.get("id")

    loja_existente = LojaIntegrada.objects.filter(id=id).first()

    if loja_existente:
        if loja_existente.ativa == True:
            messages.error(request, "Esta loja já está integrada")
        else:
            # Integrar a loja
            nova_loja = LojaIntegrada.objects.create(
                id=id,
                nome=lj_integrada.get("nome"),
                whatsapp_phone_number=lj_integrada.get("whatsapp_phone_number"),
                contact_email=lj_integrada.get("contact_email"),
                email=lj_integrada.get("email"),
                doc=lj_integrada.get("doc"),
                autorization_token=access_token,
                usuario=usuario,
            )
            messages.success(request, "Loja integrada com sucesso")
    else:
        # Integrar a loja
        nova_loja = LojaIntegrada.objects.create(
            id=id,
            nome=lj_integrada.get("nome"),
            whatsapp_phone_number=lj_integrada.get("whatsapp_phone_number"),
            contact_email=lj_integrada.get("contact_email"),
            email=lj_integrada.get("email"),
            doc=lj_integrada.get("doc"),
            autorization_token=access_token,
            usuario=usuario,
        )
        messages.success(request, "Loja integrada com sucesso")
    return redirect("nuvemshop_app:integracao")


def desativar_integracao(request):
    if request.method == "GET":

        LojaIntegrada.objects.filter(id=request.user.loja.id).delete()
        messages.info(request, "Sua loja foi desistalada com sucesso")
        return redirect("nuvemshop_app:integracao")
