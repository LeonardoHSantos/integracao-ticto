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
def Venda_Realizada(request):
    if request.method == "GET":
        return JsonResponse({"api": "-"})
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"---> Venda_Realizada:\n")
            print(data)
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



