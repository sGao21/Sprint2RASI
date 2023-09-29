from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from .logic import medicamento_logic as vl

# Create your views here.
def medicamentos_view(request):
    if request.method == 'GET':
        medicamentos= vl.get_medicamentos()
        medicamentos_dto= serializers.serialize('json',medicamentos)
        return HttpResponse(medicamentos_dto,'application/json')