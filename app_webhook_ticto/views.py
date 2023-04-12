import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    if request.method == "GET":
        return JsonResponse({"api": "-"})
    elif request.method == "POST":
        print(request.POST)
        print(json.loads(request.body))
        return JsonResponse({"api": "-"})


@csrf_exempt
def Abandono_de_Carrinho(request):
    if request.method == "GET":
        return JsonResponse({"api": "-"})
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"---> Abandono_de_Carrinho:\n {data}")
            return JsonResponse(data)
        except Exception as e:
            print(f"#### Error | Abandono_de_Carrinho: {e}")
            return JsonResponse({"code": "500", "msg": e, "local": "Abandono_de_Carrinho"})

@csrf_exempt
def Tempo_de_Teste(request):
    if request.method == "GET":
        return JsonResponse({"api": "-"})
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"---> Tempo_de_Teste:\n {data}")
            return JsonResponse(data)
        except Exception as e:
            print(f"#### Error | Tempo_de_Teste: {e}")
            return JsonResponse({"code": "500", "msg": e, "local": "Tempo_de_Teste"})

@csrf_exempt
def Aguardando_Pagamento(request):
    if request.method == "GET":
        return JsonResponse({"api": "-"})
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"---> Aguardando_Pagamento:\n {data}")
            return JsonResponse(data)
        except Exception as e:
            print(f"#### Error | Aguardando_Pagamento: {e}")
            return JsonResponse({"code": "500", "msg": e, "local": "Aguardando_Pagamento"})

@csrf_exempt
def Encerrado(request):
    if request.method == "GET":
        return JsonResponse({"api": "-"})
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"---> Encerrado:\n {data}")
            return JsonResponse(data)
        except Exception as e:
            print(f"#### Error | Encerrado: {e}")
            return JsonResponse({"code": "500", "msg": e, "local": "Encerrado"})

@csrf_exempt
def Pix_Expirado(request):
    if request.method == "GET":
        return JsonResponse({"api": "-"})
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"---> Pix_Expirado:\n {data}")
            return JsonResponse(data)
        except Exception as e:
            print(f"#### Error | Pix_Expirado: {e}")
            return JsonResponse({"code": "500", "msg": e, "local": "Pix_Expirado"})

@csrf_exempt
def Assinatura_Cancelada(request):
    if request.method == "GET":
        return JsonResponse({"api": "-"})
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"---> Assinatura_Cancelada:\n {data}")
            return JsonResponse(data)
        except Exception as e:
            print(f"#### Error | Assinatura_Cancelada: {e}")
            return JsonResponse({"code": "500", "msg": e, "local": "Assinatura_Cancelada"})

@csrf_exempt
def Pix_Gerado(request):
    if request.method == "GET":
        return JsonResponse({"api": "-"})
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"---> Pix_Gerado:\n {data}")
            return JsonResponse(data)
        except Exception as e:
            print(f"#### Error | Pix_Gerado: {e}")
            return JsonResponse({"code": "500", "msg": e, "local": "Pix_Gerado"})

@csrf_exempt
def Boleto_Atrasado(request):
    if request.method == "GET":
        return JsonResponse({"api": "-"})
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"---> Boleto_Atrasado:\n {data}")
            return JsonResponse(data)
        except Exception as e:
            print(f"#### Error | Boleto_Atrasado: {e}")
            return JsonResponse({"code": "500", "msg": e, "local": "Boleto_Atrasado"})

@csrf_exempt
def Reembolso(request):
    if request.method == "GET":
        return JsonResponse({"api": "-"})
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"---> Reembolso:\n {data}")
            return JsonResponse(data)
        except Exception as e:
            print(f"#### Error | Reembolso: {e}")
            return JsonResponse({"code": "500", "msg": e, "local": "Reembolso"})

@csrf_exempt
def Boleto_Impresso(request):
    if request.method == "GET":
        return JsonResponse({"api": "-"})
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"---> Boleto_Impresso:\n {data}")
            return JsonResponse(data)
        except Exception as e:
            print(f"#### Error | Boleto_Impresso: {e}")
            return JsonResponse({"code": "500", "msg": e, "local": "Boleto_Impresso"})

@csrf_exempt
def Venda_Realizada(request):
    if request.method == "GET":
        return JsonResponse({"api": "-"})
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"---> Venda_Realizada:\n {data}")
            return JsonResponse(data)
        except Exception as e:
            print(f"#### Error | Venda_Realizada: {e}")
            return JsonResponse({"code": "500", "msg": e, "local": "Venda_Realizada"})

@csrf_exempt
def Chargeback(request):
    if request.method == "GET":
        return JsonResponse({"api": "-"})
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"---> Chargeback:\n {data}")
            return JsonResponse(data)
        except Exception as e:
            print(f"#### Error | Chargeback: {e}")
            return JsonResponse({"code": "500", "msg": e, "local": "Chargeback"})

@csrf_exempt
def Venda_Recusada(request):
    if request.method == "GET":
        return JsonResponse({"api": "-"})
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"---> Venda_Recusada:\n {data}")
            return JsonResponse(data)
        except Exception as e:
            print(f"#### Error | Venda_Recusada: {e}")
            return JsonResponse({"code": "500", "msg": e, "local": "Venda_Recusada"})



