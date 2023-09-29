from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from .logic import cirugia_logic as vl

# Create your views here.
def cirugias_view(request):
    if request.method == 'GET':
        cirugias= vl.get_cirugias()
        cirugias_dto= serializers.serialize('json',cirugias)
        return HttpResponse(cirugias_dto,'application/json')