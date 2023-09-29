from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from .logic import paciente_logic as vl

# Create your views here.
def pacientes_view(request):
    if request.method == 'GET':
        pacientes= vl.get_pacientes()
        pacientes_dto= serializers.serialize('json',pacientes)
        return HttpResponse(pacientes_dto,'application/json')