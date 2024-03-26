from django.shortcuts import render
from libs.nuvemshop import NuvemShop

# Create your views here.
nuvemshop = NuvemShop()
PARAMETRO_CODE = "code"


# def integracao(request):
#   return render(request, "nuvemshop_app/integracao.html")


# def auth_nuvemshop(request):
def integracao(request):
    """
    Autentica a loja NuvemShop e cria uma nova instância de integração ou atualiza uma existente.
    """

    # Verifique se o parâmetro 'code' existe na URL
    code = request.GET.get(PARAMETRO_CODE, None)
    codigo = nuvemshop.auth_nuvem_shop(code=code)
    print(codigo)
    return render(request, "nuvemshop_app/integracao.html")
