from django.shortcuts import render
from libs.nuvemshop import NuvemShop



nuvemshop = NuvemShop()
PARAMETRO_CODE = "code"


def integracao(request):
    """
    Autentica a loja NuvemShop e cria uma nova instância de integração ou atualiza uma existente.
    """
    # Verifique se o parâmetro 'code' existe na URL
    code = request.GET.get(PARAMETRO_CODE, None)

    if code is not None:
        return autorizar(request, code=code)  # Chamando a função autorizar
    else:
        return render(request, "nuvemshop_app/integracao.html")


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
    print(lj_integrada)
    return render(
        request, "nuvemshop_app/integracao.html", {"lj_integrada": lj_integrada}
    )
