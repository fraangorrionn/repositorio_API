from django.shortcuts import render, redirect
from django.contrib import messages
import requests
from .forms import *
from .helper import Helper
from requests.exceptions import HTTPError

def index(request):
    return render(request, 'index.html')

def login_view(request):
    """
    Vista para autenticar usuarios en la API REST y guardar el token en la sesión.
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        response = requests.post("http://127.0.0.1:8000/api/v1/token/", data={"username": username, "password": password})
        
        if response.status_code == 200:
            tokens = response.json()
            request.session["access_token"] = tokens["access"]
            request.session["refresh_token"] = tokens["refresh"]
            print("🔹 Token almacenado:", request.session["access_token"])  # DEBUG
            return redirect("index")
        else:
            return render(request, "api/login.html", {"error": "Credenciales inválidas"})

    return render(request, "api/login.html")


# Listado de productos desde la API
def producto_listar_api(request):
    """
    Devuelve el listado de todos los productos.
    """
    token = request.session.get('access_token', None)
    headers = {'Authorization': f'Bearer {token}'} if token else {}

    response = requests.get('http://127.0.0.1:8001/productos/', headers=headers)

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

    response = requests.get(f'http://127.0.0.1:8001/productos/detallados/{id}/', headers=headers)

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

    response = requests.get('http://127.0.0.1:8001/ordenes/', headers=headers)

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

    response = requests.get('http://127.0.0.1:8001/proveedores/', headers=headers)

    if response.status_code == 200:
        proveedores = response.json()
    else:
        proveedores = []
    
    return render(request, 'api/proveedor_list.html', {"proveedores": proveedores})

# ----------------- Búsqueda Simple ----------------- #
def producto_busqueda_simple(request):
    formulario = BusquedaProductoForm(request.GET)

    if formulario.is_valid():
        helper = Helper(request)
        productos = helper.obtener_productos({'search': formulario.cleaned_data['textoBusqueda']})
        return render(request, 'api/lista_productos_api.html', {"productos": productos})

    return render(request, 'api/busqueda_producto_simple.html', {"formulario": formulario})


# ----------------- Búsqueda Avanzada de Producto ----------------- #
def producto_busqueda_avanzada(request):
    formulario = BusquedaAvanzadaProductoForm(request.GET)

    if formulario.is_valid():
        helper = Helper(request)
        productos = helper.obtener_productos(formulario.cleaned_data)
        return render(request, 'api/lista_productos_api.html', {"productos": productos})

    return render(request, 'api/busqueda_avanzada_producto.html', {"formulario": formulario})


# ----------------- Búsqueda Avanzada de Órdenes ----------------- #
def orden_busqueda_avanzada(request):
    formulario = BusquedaAvanzadaOrdenForm(request.GET)

    if formulario.is_valid():
        helper = Helper(request)
        ordenes = helper.obtener_ordenes(formulario.cleaned_data)
        return render(request, 'api/lista_ordenes_api.html', {"ordenes": ordenes})

    return render(request, 'api/busqueda_avanzada_orden.html', {"formulario": formulario})


# ----------------- Búsqueda Avanzada de Proveedores ----------------- #
def proveedor_busqueda_avanzada(request):
    formulario = BusquedaAvanzadaProveedorForm(request.GET)

    if formulario.is_valid():
        helper = Helper(request)
        proveedores = helper.obtener_proveedores(formulario.cleaned_data)
        return render(request, 'api/lista_proveedores_api.html', {"proveedores": proveedores})

    return render(request, 'api/busqueda_avanzada_proveedor.html', {"formulario": formulario})


# Páginas de error personalizadas
def mi_error_404(request, exception=None):
    return render(request, 'errores/404.html', None, None, 404)

def mi_error_500(request, exception=None):
    return render(request, 'errores/500.html', None, None, 500)