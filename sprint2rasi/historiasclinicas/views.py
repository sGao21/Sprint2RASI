from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from .logic import historiasclinicas_logic as vl

# Create your views here.
def historiasclinicas_view(request):
    if request.method == 'GET':
        historiasclinicas= vl.get_historiasclinicas()
        historiasclinicas_dto= serializers.serialize('json',historiasclinicas)
        return HttpResponse(historiasclinicas_dto,'application/json')