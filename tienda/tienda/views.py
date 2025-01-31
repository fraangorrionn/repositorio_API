from django.shortcuts import render,redirect
from django.contrib import messages

import json
from requests.exceptions import HTTPError
from django.http import HttpResponse
import requests

import os
from pathlib import Path

# Create your views here.
def index(request):
    return render(request, 'index.html')


def producto_listar_api(request):
    headers = {'Authorization': 'Bearer TU_ACCESS_TOKEN'}
    response = requests.get('http://127.0.0.1:8081/api/v1/Producto', headers=headers)

    productos = response.json()
    return render(request, 'api/producto_list.html', {"productos": productos})

    
def producto_detalle_api(request):
    headers = {'Authorization': 'Bearer TU_ACCESS_TOKEN'}
    response = requests.get('http://127.0.0.1:8081/api/v1/ProductoDetallado', headers=headers)

    productos = response.json()
    return render(request, 'api/producto_list_detallado.html', {"productos": productos})


#Páginas de Error
def mi_error_404(request,exception=None):
    return render(request, 'errores/404.html',None,None,404)

def mi_error_500(request,exception=None):
    return render(request, 'errores/500.html',None,None,500)