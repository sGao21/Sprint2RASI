from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from .logic import consulta_logic as vl

# Create your views here.
def consultas_view(request):
    if request.method == 'GET':
        consultas= vl.get_consultas()
        consultas_dto= serializers.serialize('json',consultas)
        return HttpResponse(consultas_dto,'application/json')