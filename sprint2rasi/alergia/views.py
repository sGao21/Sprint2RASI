from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from .logic import alergia_logic as vl

# Create your views here.
def alergias_view(request):
    if request.method == 'GET':
        alergias= vl.get_alergias()
        alergias_dto= serializers.serialize('json',alergias)
        return HttpResponse(alergias_dto,'application/json')