from django.shortcuts import render,redirect
from django.contrib import messages

import json
from requests.exceptions import HTTPError

import requests

import os
from pathlib import Path

# Create your views here.
def index(request):
    return render(request, 'index.html')
from django.http import HttpResponse

def orden_lista(request):
    try:
        # Realizar la solicitud GET a la API
        response = requests.get('http://127.0.0.1:8000/api/v1/')
        
        # Verificar el código de estado HTTP
        if response.status_code != 200:
            return HttpResponse(f"Error: La API devolvió el código {response.status_code}", status=response.status_code)

        # Intentar decodificar JSON
        try:
            ordenes = response.json()
        except ValueError:
            return HttpResponse("Error: La respuesta de la API no es JSON válido.", status=500)

        # Renderizar la plantilla con los datos
        return render(request, 'api/lista_api.html', {"orden_mostrar": ordenes})
    
    except requests.exceptions.RequestException as e:
        # Manejar errores de conexión
        return HttpResponse(f"Error al conectar con la API: {e}", status=500)