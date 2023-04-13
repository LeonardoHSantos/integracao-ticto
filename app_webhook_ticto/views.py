import json
import bcrypt, os
from datetime import datetime, timedelta


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
            print(" <<<<<<<<<<<< obj_database >>>>>>>>>>>> ")
            obj_database = prepapre_date(data)
            print(obj_database)
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

def prepapre_date(data):
    _payment_method = data["payment_method"]
    # ---------------------------------------------
    _product_id = data["item"]["product_id"]
    _product_name = data["item"]["product_name"]
    # ---------------------------------------------
    _useremail = data["customer"]["email"]
    _username = data["customer"]["name"]
    _password = "123456"
    _password_hash_4 = bcrypt.hashpw(_password.encode("utf8"), bcrypt.gensalt()).decode("utf-8")
    order_status = data["status"]
    _token = data["token"]
    _token_os = os.urandom(50).hex()
    _plan_started_at = datetime.now().replace(hour=0, minute=0, second=0).strftime("%Y-%m-%d %H:%M:%S")
    _plan_expiration = datetime.strftime((datetime.now().replace(hour=0, minute=0, second=0) + timedelta(days=366)), "%Y-%m-%d %H:%M:%S")
    obj_database = {
        "useremail": _useremail,
        "username": _username,
        "_password_hash_4": _password_hash_4,
        "order_status": order_status,
        "token": _token_os,
        "plan_started_at": _plan_started_at,
        "plan_expiration": _plan_expiration,
    }
    return obj_database

