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
def nova_ordem(request):
    if request.method == "GET":
        return JsonResponse({"api": "-"})

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            print(data)
            return JsonResponse(data)
        except Exception as e:
            print(e)
            return JsonResponse({"code": "500", "msg": "falha ao processar (webhook)"})



