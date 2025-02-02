from django.shortcuts import render
from django.contrib import messages
import requests

# Vista para la página principal
def index(request):
    return render(request, 'index.html')

# Listado de productos desde la API
def producto_listar_api(request):
    """
    Devuelve el listado de todos los productos.
    """
    token = request.session.get('access_token', None)
    headers = {'Authorization': f'Bearer {token}'} if token else {}

    response = requests.get('http://127.0.0.1:8001/api/productos/', headers=headers)

    if response.status_code == 200:
        productos = response.json()
    else:
        productos = []  # Si la API falla, devolver lista vacía

    return render(request, 'api/lista_productos_api.html', {"productos": productos})


def producto_detalle_api(request, id):
    """
    Devuelve el detalle de un producto específico por su ID.
    """
    token = request.session.get('access_token', None)
    headers = {'Authorization': f'Bearer {token}'} if token else {}

    response = requests.get(f'http://127.0.0.1:8001/api/productos/detallados/{id}/', headers=headers)

    if response.status_code == 200:
        producto = response.json()
    else:
        producto = None  # Si la API falla, no mostrar producto

    return render(request, 'api/lista_productos_detallada_api.html', {"producto": producto})

def ordenes_listar_api(request):
    """
    Devuelve el listado de todas las órdenes con autenticación OAUTH 2.
    """
    token = request.session.get('access_token', None)
    headers = {'Authorization': f'Bearer {token}'} if token else {}

    response = requests.get('http://127.0.0.1:8001/api/ordenes/', headers=headers)

    if response.status_code == 200:
        ordenes = response.json()
    else:
        ordenes = []
    
    return render(request, 'api/orden_list.html', {"ordenes": ordenes})


def proveedores_listar_api(request):
    """
    Devuelve el listado de todos los proveedores con autenticación OAUTH 2.
    """
    token = request.session.get('access_token', None)
    headers = {'Authorization': f'Bearer {token}'} if token else {}

    response = requests.get('http://127.0.0.1:8001/api/proveedores/', headers=headers)

    if response.status_code == 200:
        proveedores = response.json()
    else:
        proveedores = []
    
    return render(request, 'api/proveedor_list.html', {"proveedores": proveedores})

# Páginas de error personalizadas
def mi_error_404(request, exception=None):
    return render(request, 'errores/404.html', None, None, 404)

def mi_error_500(request, exception=None):
    return render(request, 'errores/500.html', None, None, 500)