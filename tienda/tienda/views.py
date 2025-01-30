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
    
def orden_lista(request):
    headers = {'Authorization': 'Bearer '+request.session["token"]} 
    print(headers)
    response = requests.get('http://127.0.0.1:8000/api/v1/orden',headers=headers)
    ordenes = response.json()
    return render(request, 'api/orden_api.html',{"orden_mostrar": ordenes})

def producto_lista(request):
    headers = {'Authorization': 'Bearer '+request.session["token"]} 
    print(headers)
    response = requests.get('http://127.0.0.1:8000/api/v1/producto',headers=headers)
    productos = response.json()
    return render(request, 'api/producto_api.html',{"producto_mostrar": productos})

def usuario_lista(request):
    headers = {'Authorization': 'Bearer '+request.session["token"]} 
    print(headers)
    response = requests.get('http://127.0.0.1:8000/api/v1/orden',headers=headers)
    usuarios = response.json()
    return render(request, 'api/usuario_api.html',{"usuario_mostrar": usuarios})

#Páginas de Error
def mi_error_404(request,exception=None):
    return render(request, 'errores/404.html',None,None,404)

def mi_error_500(request,exception=None):
    return render(request, 'errores/500.html',None,None,500)