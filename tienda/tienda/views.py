from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
import json
from requests.exceptions import HTTPError
import requests
from pathlib import Path
import xml.etree.ElementTree as ET
from .utils import manejar_errores_api, manejar_excepciones_api 
import environ
import os

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'),True)
env = environ.Env()

# PREGUNTA 1: ¿Qué pasaría si cambia la versión de la API?
# En lugar de escribir manualmente la URL en cada vista, usamos una variable global.
# Si la API cambia a `v2`, solo debemos actualizar esta variable y no modificar todo el código.
BASE_API_URL = "https://fraangorrionn.pythonanywhere.com/api/v1/"
BASE_API_URL_local = "http://127.0.0.1:8000/api/v1/"

def index(request):
    return render(request, 'index.html')

# ------------------ Listado de Productos ------------------ #
def producto_listar_api(request):
    """
    Devuelve el listado de todos los productos con autenticación OAUTH 2 según el rol del usuario.
    """
    if not request.user.is_anonymous:
        if request.user.rol == 1:  # Admin
            headers = {'Authorization': f'Bearer {env("Admin")}'}
        elif request.user.rol == 2:  # Cliente
            headers = {'Authorization': f'Bearer {env("Cliente")}'}
        else:  # Gerente
            headers = {'Authorization': f'Bearer {env("Gerente")}'}
    else:
        headers = {'Authorization': f'Bearer {env("Cliente")}'}

    response = requests.get(BASE_API_URL + "productos/", headers=headers)

    # PREGUNTA 2: ¿Qué pasa si la API cambia de JSON a XML?
    # En lugar de asumir siempre JSON, detectamos el formato de respuesta y lo procesamos adecuadamente.
    content_type = response.headers.get("Content-Type", "")
    if "application/json" in content_type:
        productos = response.json()
    elif "application/xml" in content_type:
        productos = ET.fromstring(response.text)  # Convierte XML a objeto
    else:
        productos = response.text  # Si el formato es desconocido, tratarlo como texto plano

    return render(request, 'api/lista_productos_api.html', {"productos": productos})


# ------------------ Detalle de un Producto ------------------ #
def producto_detalle_api(request, id):
    """
    Devuelve el detalle de un producto específico por su ID con autenticación OAUTH 2 según el rol del usuario.
    """
    if not request.user.is_anonymous:
        if request.user.rol == 1:  # Admin
            headers = {'Authorization': f'Bearer {env("Admin")}'}
        elif request.user.rol == 2:  # Cliente
            headers = {'Authorization': f'Bearer {env("Cliente")}'}
        else:  # Gerente
            headers = {'Authorization': f'Bearer {env("Gerente")}'}
    else:
        headers = {'Authorization': f'Bearer {env("Cliente")}'}

    response = requests.get(BASE_API_URL + f"productos/detallados/{id}/", headers=headers)

    producto = response.json() if response.status_code == 200 else None
    
    return render(request, 'api/lista_productos_detallada_api.html', {"producto": producto})


# ------------------ Listado de Órdenes ------------------ #
def ordenes_listar_api(request):
    """
    Devuelve el listado de todas las órdenes con autenticación OAUTH 2 según el rol del usuario.
    """
    if not request.user.is_anonymous:
        if request.user.rol == 1:  # Admin
            headers = {'Authorization': f'Bearer {env("Admin")}'}
        elif request.user.rol == 2:  # Cliente
            headers = {'Authorization': f'Bearer {env("Cliente")}'}
        else:  # Gerente
            headers = {'Authorization': f'Bearer {env("Gerente")}'}
    else:
        headers = {'Authorization': f'Bearer {env("Cliente")}'}

    response = requests.get(BASE_API_URL + "ordenes/", headers=headers)

    ordenes = response.json() if response.status_code == 200 else []
    
    return render(request, 'api/orden_list.html', {"ordenes": ordenes})


# ------------------ Listado de Proveedores ------------------ #
def proveedores_listar_api(request):
    """
    Devuelve el listado de todos los proveedores con autenticación OAUTH 2 según el rol del usuario.
    """
    if not request.user.is_anonymous:
        if request.user.rol == 1:  # Admin
            headers = {'Authorization': f'Bearer {env("Admin")}'}
        elif request.user.rol == 2:  # Cliente
            headers = {'Authorization': f'Bearer {env("Cliente")}'}
        else:  # Gerente
            headers = {'Authorization': f'Bearer {env("Gerente")}'}
    else:
        headers = {'Authorization': f'Bearer {env("Cliente")}'}

    response = requests.get(BASE_API_URL + "proveedores/", headers=headers)

    proveedores = response.json() if response.status_code == 200 else []
    
    return render(request, 'api/proveedor_list.html', {"proveedores": proveedores})

def crear_cabecera():
    return {
        'Authorization': f'Bearer {env("Admin")}',
        "Content-Type": "application/json"
    }

# PREGUNTA 3: ¿Siempre debemos tratar los errores en cada petición?
# No, por eficiencia, es mejor tener funciones centralizadas como `manejar_errores_api` y `manejar_excepciones_api`
# para no repetir código innecesario y evitar errores en cada vista.

# ----------------- Búsqueda Simple de Producto ----------------- #
def producto_busqueda_simple(request):
    if request.GET:
        formulario = BusquedaProductoForm(request.GET)
        if formulario.is_valid():
            try:
                headers = crear_cabecera()
                response = requests.get(
                    BASE_API_URL + 'productos/busqueda/',
                    headers=headers,
                    params={'search': formulario.cleaned_data.get("textoBusqueda")}
                )

                # ✅ PREGUNTA 2: Manejo de múltiples formatos (JSON, XML, etc.)
                content_type = response.headers.get("Content-Type", "")
                if "application/json" in content_type:
                    productos = response.json()
                elif "application/xml" in content_type:
                    productos = ET.fromstring(response.text)
                else:
                    productos = response.text

                if response.status_code == requests.codes.ok:
                    return render(request, 'api/busqueda_producto_simple.html', {"productos": productos, "formulario": formulario})
                else:
                    return manejar_errores_api(response, request, formulario, "api/busqueda_producto_simple.html")

            except Exception as err:
                return manejar_excepciones_api(err, request)

        return redirect(request.META.get("HTTP_REFERER", "index"))

    formulario = BusquedaProductoForm()
    return render(request, 'api/busqueda_producto_simple.html', {"formulario": formulario})



# ----------------- Búsqueda Avanzada de Producto ----------------- #
def producto_busqueda_avanzada(request):
    if request.GET:
        formulario = BusquedaAvanzadaProductoForm(request.GET)
        if formulario.is_valid():
            try:
                headers = crear_cabecera()
                response = requests.get(
                    BASE_API_URL + 'productos/busqueda-avanzada/',
                    headers=headers,
                    params=formulario.cleaned_data
                )

                content_type = response.headers.get("Content-Type", "")
                if "application/json" in content_type:
                    productos = response.json()
                elif "application/xml" in content_type:
                    productos = ET.fromstring(response.text)
                else:
                    productos = response.text

                if response.status_code == requests.codes.ok:
                    return render(request, 'api/lista_productos_api.html', {"productos": productos, "formulario": formulario})
                else:
                    return manejar_errores_api(response, request, formulario, "api/busqueda_avanzada_producto.html")

            except Exception as err:
                return manejar_excepciones_api(err, request)

        return redirect(request.META.get("HTTP_REFERER", "index"))

    formulario = BusquedaAvanzadaProductoForm()
    return render(request, 'api/busqueda_avanzada_producto.html', {"formulario": formulario})


# ----------------- Búsqueda Avanzada de Órdenes ----------------- #
def orden_busqueda_avanzada(request):
    if request.GET:
        formulario = BusquedaAvanzadaOrdenForm(request.GET)
        if formulario.is_valid():
            try:
                headers = crear_cabecera()
                response = requests.get(
                    BASE_API_URL + 'ordenes/busqueda-avanzada/',
                    headers=headers,
                    params=formulario.cleaned_data
                )

                content_type = response.headers.get("Content-Type", "")
                if "application/json" in content_type:
                    ordenes = response.json()
                elif "application/xml" in content_type:
                    ordenes = ET.fromstring(response.text)
                else:
                    ordenes = response.text

                if response.status_code == requests.codes.ok:
                    return render(request, 'api/lista_ordenes_api.html', {"ordenes": ordenes, "formulario": formulario})
                else:
                    return manejar_errores_api(response, request, formulario, "api/busqueda_avanzada_orden.html")

            except Exception as err:
                return manejar_excepciones_api(err, request)

        return redirect(request.META.get("HTTP_REFERER", "index"))

    formulario = BusquedaAvanzadaOrdenForm()
    return render(request, 'api/busqueda_avanzada_orden.html', {"formulario": formulario})


# ----------------- Búsqueda Avanzada de Proveedores ----------------- #
def proveedor_busqueda_avanzada(request):
    if request.GET:
        formulario = BusquedaAvanzadaProveedorForm(request.GET)
        if formulario.is_valid():
            try:
                headers = crear_cabecera()
                response = requests.get(
                    BASE_API_URL + 'proveedores/busqueda-avanzada/',
                    headers=headers,
                    params=formulario.cleaned_data
                )

                content_type = response.headers.get("Content-Type", "")
                if "application/json" in content_type:
                    proveedores = response.json()
                elif "application/xml" in content_type:
                    proveedores = ET.fromstring(response.text)
                else:
                    proveedores = response.text

                if response.status_code == requests.codes.ok:
                    return render(request, 'api/lista_proveedores_api.html', {"proveedores": proveedores, "formulario": formulario})
                else:
                    return manejar_errores_api(response, request, formulario, "api/busqueda_avanzada_proveedor.html")

            except Exception as err:
                return manejar_excepciones_api(err, request)

        return redirect(request.META.get("HTTP_REFERER", "index"))

    formulario = BusquedaAvanzadaProveedorForm()
    return render(request, 'api/busqueda_avanzada_proveedor.html', {"formulario": formulario})


# Páginas de error personalizadas
def mi_error_404(request, exception=None):
    return render(request, 'errores/404.html', None, None, 404)

def mi_error_500(request, exception=None):
    return render(request, 'errores/500.html', None, None, 500)