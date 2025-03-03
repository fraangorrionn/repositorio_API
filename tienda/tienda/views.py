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
import json
from .helper import helper
from .cliente_api import *
from dotenv import set_key
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'),True)
env = environ.Env()

# PREGUNTA 1: ¿Qué pasaría si cambia la versión de la API?
# En lugar de escribir manualmente la URL en cada vista, usamos una variable global.
# Si la API cambia a `v2`, solo debemos actualizar esta variable y no modificar todo el código.

BASE_API_URL = env("BASE_API_URL")
version = env("version")

def index(request):
    return render(request, 'index.html')

def crear_cabecera():
    return {
        'Authorization': 'Bearer '+env("Admin"),
        "Content-Type": "application/json"
        }


 # ------------------ Listado de Productos ------------------ #
def producto_listar_api(request):
    if not request.user.is_anonymous:
        if request.user.rol == 1:  # Admin
            headers = {'Authorization': f'Bearer {env("Admin")}'}
        elif request.user.rol == 2:  # Cliente
            headers = {'Authorization': f'Bearer {env("Cliente")}'}
        else:  # Gerente
            headers = {'Authorization': f'Bearer {env("Gerente")}'}
    else:
        headers = {'Authorization': f'Bearer {env("Cliente")}'}

    try:
        response = requests.get(f"{BASE_API_URL}/productos/", headers=headers)
        response.raise_for_status()  # Lanza error si la respuesta no es 200

        productos = response.json()  # Intentar convertir a JSON
        if not isinstance(productos, list):
            raise ValueError("La API no devolvió una lista de productos")

    except (requests.RequestException, ValueError) as e:
        print(f"❌ Error en producto_listar_api: {e}")
        productos = []  # Devolver lista vacía en caso de error

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

    response = requests.get(f"{BASE_API_URL}/productos/", headers=headers)

    if response.status_code == 200:
        productos = response.json()
        for producto in productos:
            if "id" not in producto:
                print(f"⚠️ Advertencia: Producto sin ID - {producto}")
    else:
        productos = []
    
    return render(request, 'api/lista_productos_detallada_api.html', {"producto": producto})


def favoritos_listar_api(request):
    if not request.user.is_anonymous:
        if request.user.rol == 1:
            headers = {'Authorization': f'Bearer {env("Admin")}'}
        elif request.user.rol == 2:
            headers = {'Authorization': f'Bearer {env("Cliente")}'}
        else:
            headers = {'Authorization': f'Bearer {env("Gerente")}'}
    else:
        headers = {'Authorization': f'Bearer {env("Cliente")}'}

    try:
        response = requests.get(f"{BASE_API_URL}/favoritos/", headers=headers)
        response.raise_for_status()

        favoritos = response.json()
        if not isinstance(favoritos, list):
            raise ValueError("La API no devolvió una lista de favoritos")

    except (requests.RequestException, ValueError) as e:
        print(f"❌ Error en favoritos_listar_api: {e}")
        favoritos = []

    return render(request, 'api/favoritos_list.html', {"favoritos": favoritos})


# ------------------ Listado de Órdenes ------------------ #
def ordenes_listar_api(request):
    if not request.user.is_anonymous:
        if request.user.rol == 1:
            headers = {'Authorization': f'Bearer {env("Admin")}'}
        elif request.user.rol == 2:
            headers = {'Authorization': f'Bearer {env("Cliente")}'}
        else:
            headers = {'Authorization': f'Bearer {env("Gerente")}'}
    else:
        headers = {'Authorization': f'Bearer {env("Cliente")}'}

    try:
        response = requests.get(f"{BASE_API_URL}/ordenes/", headers=headers)
        response.raise_for_status()

        ordenes = response.json()
        if not isinstance(ordenes, list):
            raise ValueError("La API no devolvió una lista de órdenes")

    except (requests.RequestException, ValueError) as e:
        print(f"❌ Error en ordenes_listar_api: {e}")
        ordenes = []

    return render(request, 'api/orden_list.html', {"ordenes": ordenes})


# ------------------ Listado de Proveedores ------------------ #
def proveedores_listar_api(request):
    if not request.user.is_anonymous:
        if request.user.rol == 1:
            headers = {'Authorization': f'Bearer {env("Admin")}'}
        elif request.user.rol == 2:
            headers = {'Authorization': f'Bearer {env("Cliente")}'}
        else:
            headers = {'Authorization': f'Bearer {env("Gerente")}'}
    else:
        headers = {'Authorization': f'Bearer {env("Cliente")}'}

    try:
        response = requests.get(f"{BASE_API_URL}/proveedores/", headers=headers)
        response.raise_for_status()

        proveedores = response.json()
        if not isinstance(proveedores, list):
            raise ValueError("La API no devolvió una lista de proveedores")

    except (requests.RequestException, ValueError) as e:
        print(f"❌ Error en proveedores_listar_api: {e}")
        proveedores = []

    return render(request, 'api/proveedor_list.html', {"proveedores": proveedores})


def usuario_listar_api(request):
    if not request.user.is_anonymous:
        if request.user.rol == 1:
            headers = {'Authorization': f'Bearer {env("Admin")}'}
        elif request.user.rol == 2:
            headers = {'Authorization': f'Bearer {env("Cliente")}'}
        else:
            headers = {'Authorization': f'Bearer {env("Gerente")}'}
    else:
        headers = {'Authorization': f'Bearer {env("Cliente")}'}

    try:
        response = requests.get(f"{BASE_API_URL}/usuarios/", headers=headers)
        response.raise_for_status()

        usuarios = response.json()
        if not isinstance(usuarios, list):
            raise ValueError("La API no devolvió una lista de usuarios")

    except (requests.RequestException, ValueError) as e:
        print(f"❌ Error en usuario_listar_api: {e}")
        usuarios = []

    return render(request, 'api/lista_usuarios_api.html', {"usuarios": usuarios})



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

#--------------------------------------Formularios POST-------------------------------------------------
def crear_producto(request):
    # Vista para crear un producto en la API.
    
    if request.method == "POST":
        try:
            formulario = ProductoForm(request.POST)

            headers = crear_cabecera() 
            
            datos = formulario.data.copy()
            datos["nombre"] = request.POST.get("nombre")
            datos["tipo"] = request.POST.get("tipo")
            datos["precio"] = request.POST.get("precio")
            datos["stock"] = request.POST.get("stock")
            datos["descripcion"] = request.POST.get("descripcion")

            response = requests.post(
                BASE_API_URL + version + 'productos/crear/',
                headers=headers,
                data=json.dumps(datos)
            )

            if response.status_code == requests.codes.ok:
                messages.success(request, response.json())
                return redirect("producto_listar_api")
            else:
                return manejar_errores_api(response, request, formulario, "formularios/Producto/crear_producto.html")

        except Exception as err:
            return manejar_excepciones_api(err, request)  

    else:
        formulario = ProductoForm(None)

    return render(request, 'formularios/Producto/crear_producto.html', {"formulario": formulario})


def crear_orden(request):
    if request.method == "POST":
        try:
            formulario = OrdenForm(request.POST, request.FILES)  # ✅ Se añade request.FILES para manejar archivos

            headers = crear_cabecera()

            datos = formulario.data.copy()
            datos["usuario"] = request.POST.get("usuario")
            datos["total"] = request.POST.get("total")
            datos["estado"] = request.POST.get("estado")
            datos["metodo_pago"] = request.POST.get("metodo_pago")

            # ✅ Manejo del archivo adjunto
            files = request.FILES.get("archivo_adjunto", None)
            files_payload = {"archivo_adjunto": (files.name, files.read(), files.content_type)} if files else None

            response = requests.post(
                BASE_API_URL + version + 'ordenes/crear/',
                headers=headers,
                data=datos,
                files=files_payload  # ✅ Se agrega el archivo al envío
            )

            if response.status_code == requests.codes.ok:
                messages.success(request, response.json())
                return redirect("ordenes_listar_api")
            else:
                return manejar_errores_api(response, request, formulario, "formularios/Orden/crear_orden.html")

        except Exception as err:
            return manejar_excepciones_api(err, request)

    else:
        formulario = OrdenForm(None)

    return render(request, 'formularios/Orden/crear_orden.html', {"formulario": formulario})


def crear_proveedor(request):
    if request.method == "POST":
        try:
            formulario = ProveedorForm(request.POST)

            headers = crear_cabecera()

            datos = formulario.data.copy()
            datos["productos"] = request.POST.getlist("productos")
            datos["nombre"] = request.POST.get("nombre")
            datos["contacto"] = request.POST.get("contacto")
            datos["telefono"] = request.POST.get("telefono")
            datos["correo"] = request.POST.get("correo")

            response = requests.post(
                BASE_API_URL + version + 'proveedores/crear/',
                headers=headers,
                data=json.dumps(datos)
            )

            if response.status_code == requests.codes.ok:
                messages.success(request, response.json())
                return redirect("proveedores_listar_api")
            else:
                return manejar_errores_api(response, request, formulario, "formularios/Proveedor/crear_proveedor.html")

        except Exception as err:
            return manejar_excepciones_api(err, request)  

    else:
        formulario = ProveedorForm(None)

    return render(request, 'formularios/Proveedor/crear_proveedor.html', {"formulario": formulario})



def crear_favorito(request):
    if request.method == "POST":
        try:
            formulario = FavoritosForm(request.POST)
            headers = crear_cabecera()

            datos = formulario.data.copy()
            datos["usuario"] = request.POST.get("usuario")
            datos["producto"] = request.POST.get("producto")
            datos["prioridad"] = request.POST.get("prioridad")
            datos["notas"] = request.POST.get("notas")

            response = requests.post(
                BASE_API_URL + version + 'favoritos/crear/',
                headers=headers,
                data=json.dumps(datos)
            )

            if response.status_code == requests.codes.ok:
                messages.success(request, response.json())
                return redirect("favoritos_listar_api")
            else:
                return manejar_errores_api(response, request, formulario, "formularios/Favoritos/crear_favoritos.html")

        except Exception as err:
            return manejar_excepciones_api(err, request)

    else:
        formulario = FavoritosForm(None)

    return render(request, 'formularios/Favoritos/crear_favoritos.html', {"formulario": formulario})


def crear_usuario(request):
    if request.method == "POST":
        try:
            formulario = UsuarioForm(request.POST)

            headers = crear_cabecera() 
            
            datos = formulario.data.copy()
            datos["username"] = request.POST.get("username")
            datos["email"] = request.POST.get("email")
            datos["password"] = request.POST.get("password")
            datos["rol"] = request.POST.get("rol")
            datos["direccion"] = request.POST.get("direccion")
            datos["telefono"] = request.POST.get("telefono")

            response = requests.post(
                BASE_API_URL + version + 'usuarios/crear/',
                headers=headers,
                data=json.dumps(datos),
            )

            if response.status_code == 201:
                messages.success(request, response.json())
                return redirect("usuario_listar_api")
            else:
                return manejar_errores_api(response, request, formulario, "formularios/Usuario/crear_usuario.html")

        except Exception as err:
            return manejar_excepciones_api(err, request)  

    else:
        formulario = UsuarioForm(None)

    return render(request, "formularios/Usuario/crear_usuario.html", {"formulario": formulario})




#--------------------------------------Formularios OBTENER-------------------------------------------------

def obtener_producto(request, producto_id):
    # Vista para obtener un producto desde la API usando el helper.

    producto = helper.obtener_producto(producto_id)
    return render(request, 'formularios/Producto/mostrar_producto.html', {"producto": producto})

def obtener_orden(request, orden_id):
    # Vista para obtener una orden desde la API usando el helper.
    
    orden = helper.obtener_orden(orden_id)
    return render(request, 'formularios/Orden/mostrar_orden.html', {"orden": orden})

def obtener_proveedor(request, proveedor_id):
    proveedor = helper.obtener_proveedor(proveedor_id)
    print("Datos recibidos:", proveedor)
    return render(request, 'formularios/Proveedor/mostrar_proveedor.html', {"proveedor": proveedor})

def obtener_favoritos(request, favorito_id):
    favorito = helper.obtener_favorito(favorito_id)
    print("Datos recibidos:", favorito)
    return render(request, 'formularios/Favoritos/mostrar_favoritos.html', {"favorito": favorito})


#--------------------------------------Formularios PUT-------------------------------------------------
def editar_producto(request, producto_id):
    # Vista para editar un producto en la API.
    
    datosFormulario = None

    if request.method == "POST":
        datosFormulario = request.POST 

    producto = helper.obtener_producto(producto_id)

    formulario = ProductoForm(datosFormulario,
        initial={
            'nombre': producto['nombre'],
            'tipo': producto["tipo"],
            'precio': producto['precio'],
            'stock': producto['stock'],
            'descripcion': producto['descripcion'],
        }
    )

    if request.method == "POST":
        formulario = ProductoForm(request.POST)
        datos = request.POST.copy()

        cliente = cliente_api(
            env("Admin"),
            "PUT",
            'productos/' + str(producto_id) + '/actualizar/',
            datos
        )
        
        cliente.realizar_peticion_api()

        if cliente.es_respuesta_correcta():
            mensaje = cliente.datosRespuesta

            messages.success(request, mensaje)

            return redirect("producto_listar_api", producto_id=producto_id)
        else:
            if cliente.es_error_validacion_datos():
                cliente.incluir_errores_formulario(formulario)
            else:
                return manejar_errores_api(request, cliente.codigoRespuesta)

    return render(request, 'formularios/Producto/editar_producto.html', {"formulario": formulario, "producto": producto})


def editar_orden(request, orden_id):
    # Vista para editar una orden en la API.

    datosFormulario = None

    if request.method == "POST":
        datosFormulario = request.POST 

    orden = helper.obtener_orden(orden_id)

    formulario = OrdenForm(datosFormulario,
        initial={
            'usuario': orden['usuario'],
            'total': orden['total'],
            'estado': orden['estado'],
            'metodo_pago': orden['metodo_pago'],
        }
    )

    if request.method == "POST":
        formulario = OrdenForm(request.POST, request.FILES)  # Permitir subida de archivos
        datos = request.POST.copy()
        archivo = request.FILES.get("archivo_adjunto", None)

        # Crear diccionario de datos para enviar al backend
        payload = {
            "usuario": datos.get("usuario"),
            "total": datos.get("total"),
            "estado": datos.get("estado"),
            "metodo_pago": datos.get("metodo_pago"),
        }

        # Adjuntar archivo si se subió uno
        archivos = {"archivo_adjunto": archivo} if archivo else {}

        response = requests.put(
            f"{BASE_API_URL}{version}ordenes/{orden_id}/editar/",
            headers=crear_cabecera(),
            data=payload,
            files=archivos
        )

        if response.status_code == 200:
            messages.success(request, "Orden editada correctamente.")
            return redirect("orden_listar_api")
        else:
            return manejar_errores_api(response, request, formulario, "formularios/Orden/editar_orden.html")

    return render(request, 'formularios/Orden/editar_orden.html', {"formulario": formulario, "orden": orden})



def editar_proveedor(request, proveedor_id):

    datosFormulario = None

    if request.method == "POST":
        datosFormulario = request.POST 

    proveedor = helper.obtener_proveedor(proveedor_id)

    formulario = ProveedorForm(datosFormulario,
        initial={
            'nombre': proveedor['nombre'],
            'contacto': proveedor["contacto"],
            'telefono': proveedor['telefono'],
            'correo': proveedor['correo'],
            'productos': [prod['id'] for prod in proveedor['productos']],
        }
    )

    if request.method == "POST":
        formulario = ProveedorForm(request.POST)
        datos = request.POST.copy()
        datos["productos"] = request.POST.getlist("productos")
        
        cliente = cliente_api(
            env("Admin"),
            "PUT",
            'proveedores/' + str(proveedor_id) + '/editar/',
            datos
        )
        
        cliente.realizar_peticion_api()

        if cliente.es_respuesta_correcta():

            mensaje = cliente.datosRespuesta

            messages.success(request, mensaje)

            return redirect("proveedores_listar_api", proveedor_id=proveedor_id)
        else:
            if cliente.es_error_validacion_datos():
                cliente.incluir_errores_formulario(formulario)
            else:
                return manejar_errores_api(request, cliente.codigoRespuesta)

    return render(request, 'formularios/Proveedor/editar_proveedor.html', {"formulario": formulario, "proveedor": proveedor})

def editar_favoritos(request, favorito_id):
    datosFormulario = None

    # Si el usuario envió datos (POST), se almacenan en `datosFormulario`
    if request.method == "POST":
        datosFormulario = request.POST 

    # Obtener los datos actuales del favorito desde la API
    favorito = helper.obtener_favorito(favorito_id) 
    print("📩 DEBUG - favorito['usuario']:", favorito["usuario"])

    # Crear el Formulario con Datos Iniciales
    formulario = FavoritosForm(datosFormulario,
        initial={
            'usuario': favorito["usuario"]["id"],
            'producto': favorito["producto"]["id"],
            'prioridad': favorito['prioridad'],
            'notas': favorito['notas']
        }
    )

    # Si el usuario envió un formulario (POST), procesamos los datos
    if request.method == "POST":
        formulario = FavoritosForm(request.POST)
        datos = request.POST.copy()
        datos["usuario"] = request.POST.get("usuario")
        datos["producto"] = request.POST.get("producto")
        datos["prioridad"] = request.POST.get("prioridad")
        datos["notas"] = request.POST.get("notas")
        
        cliente = cliente_api(
            env("Admin"),
            "PUT",
            'favoritos/editar/' + str(favorito_id),
            datos
        )
        
        cliente.realizar_peticion_api()
        print("📩 DEBUG - Datos enviados a la API:", datos)
        print("📩 DEBUG - Código de respuesta API:", cliente.codigoRespuesta)

        # Manejar la Respuesta de la API
        if cliente.es_respuesta_correcta():
            # Guardar el mensaje directamente como lo envía la API
            mensaje = cliente.datosRespuesta

            # Guardar mensaje en Django Messages
            messages.success(request, mensaje)

            return redirect("favoritos_listar_api", favorito_id=favorito_id)
        else:
            if cliente.es_error_validacion_datos():
                cliente.incluir_errores_formulario(formulario)
            else:
                return manejar_errores_api(request, cliente.codigoRespuesta)

    return render(request, 'formularios/Favoritos/editar_favoritos.html', {"formulario": formulario, "favorito": favorito})


#--------------------------------------Formularios PATCH-------------------------------------------------

def actualizar_nombre_producto(request, producto_id):
    # Vista para actualizar solo el nombre de un producto usando PATCH.


    datosFormulario = None

    if request.method == "POST":
        datosFormulario = request.POST

    producto = helper.obtener_producto(producto_id)

    formulario = ProductoActualizarNombreForm(datosFormulario,
        initial={
            'nombre': producto['nombre'],
        }
    )

    if request.method == "POST":
        try:
            formulario = ProductoActualizarNombreForm(request.POST)
            headers = crear_cabecera()
            datos = request.POST.copy()

            response = requests.patch(
                BASE_API_URL + version + 'productos/' + str(producto_id) + '/actualizar-nombre/',
                headers=headers,
                data=json.dumps(datos)
            )

            if response.status_code == requests.codes.ok:
                return redirect("producto_listar_api", producto_id=producto_id)
            else:
                print(response.status_code)
                response.raise_for_status()

        except HTTPError as http_err:
            print(f'Hubo un error en la petición: {http_err}')

            if response.status_code == 400:
                errores = response.json()
                for error in errores:
                    formulario.add_error(error, errores[error])

                return render(request, 
                            'formularios/Producto/actualizar_nombre.html',
                            {"formulario": formulario, "producto": producto})
            else:
                return mi_error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)

    return render(request, 'formularios/Producto/actualizar_nombre.html', {"formulario": formulario, "producto": producto})


def actualizar_estado_orden(request, orden_id):
    # Vista para actualizar solo el estado y el archivo adjunto de una orden en la API.
    
    datosFormulario = None

    if request.method == "POST":
        datosFormulario = request.POST
        archivo = request.FILES.get('archivo_adjunto')

    orden = helper.obtener_orden(orden_id)

    formulario = OrdenActualizarEstadoForm(datosFormulario,
        initial={
            'estado': orden['estado'],
        }
    )

    if request.method == "POST":
        try:
            formulario = OrdenActualizarEstadoForm(request.POST, request.FILES)
            headers = crear_cabecera()

            datos = request.POST.copy()
            files = {'archivo_adjunto': archivo} if archivo else {}

            response = requests.patch(
                BASE_API_URL + version + 'ordenes/' + str(orden_id) + '/actualizar-estado/',
                headers=headers,
                data=datos,
                files=files  # Enviar el archivo en la petición
            )

            if response.status_code == requests.codes.ok:
                return redirect("orden_listar_api", orden_id=orden_id)
            else:
                print(response.status_code)
                response.raise_for_status()

        except HTTPError as http_err:
            print(f'Hubo un error en la petición: {http_err}')

            if response.status_code == 400:
                errores = response.json()
                for error in errores:
                    formulario.add_error(error, errores[error])

                return render(request, 
                            'formularios/Orden/actualizar_estado_orden.html',
                            {"formulario": formulario, "orden": orden})
            else:
                return mi_error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)

    return render(request, 'formularios/Orden/actualizar_estado_orden.html', {"formulario": formulario, "orden": orden})

def actualizar_contacto_proveedor(request, proveedor_id):
    """
    Vista para actualizar solo el contacto de un proveedor en la API.
    """

    datosFormulario = None

    if request.method == "POST":
        datosFormulario = request.POST

    # Obtener los datos actuales del proveedor desde la API
    proveedor = helper.obtener_proveedor(proveedor_id)

    formulario = ProveedorActualizarContactoForm(datosFormulario,
        initial={
            'contacto': proveedor['contacto'],
        }
    )

    if request.method == "POST":
        try:
            formulario = ProveedorActualizarContactoForm(request.POST)
            headers = crear_cabecera()
            datos = request.POST.copy()

            response = requests.patch(
                BASE_API_URL + version + 'proveedores/' + str(proveedor_id) + '/actualizar-contacto/',
                headers=headers,
                data=json.dumps(datos)
            )

            if response.status_code == requests.codes.ok:
                return redirect("proveedores_listar_api", proveedor_id=proveedor_id)
            else:
                print(response.status_code)
                response.raise_for_status()

        except HTTPError as http_err:
            print(f'Hubo un error en la petición: {http_err}')

            if response.status_code == 400:
                errores = response.json()
                for error in errores:
                    formulario.add_error(error, errores[error])

                return render(request, 
                            'formularios/Proveedor/actualizar_contacto.html',
                            {"formulario": formulario, "proveedor": proveedor})
            else:
                return mi_error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)

    return render(request, 'formularios/Proveedor/actualizar_contacto.html', {"formulario": formulario, "proveedor": proveedor})

def actualizar_prioridad_favoritos(request, favorito_id):
    datosFormulario = None

    if request.method == "POST":
        datosFormulario = request.POST

    favorito = helper.obtener_favorito(favorito_id)
    formulario = FavoritosActualizarPrioridadForm(datosFormulario,
        initial={
            'prioridad': favorito['prioridad'],
            'notas': favorito['notas'],
        }
    )

    if request.method == "POST":
        try:
            formulario = FavoritosActualizarPrioridadForm(request.POST)
            headers = crear_cabecera()
            datos = request.POST.copy()
            response = requests.patch(
                BASE_API_URL + version + 'favoritos/actualizar-prioridad/' + str(favorito_id),
                headers=headers,
                data=json.dumps(datos)
            )
            if response.status_code == requests.codes.ok:
                return redirect("favoritos_listar_api", favorito_id=favorito_id)
            else:
                print(response.status_code)
                response.raise_for_status()

        except HTTPError as http_err:
            print(f'Hubo un error en la petición: {http_err}')

            if response.status_code == 400:
                errores = response.json()
                for error in errores:
                    formulario.add_error(error, errores[error])
                return render(request, 
                            'formularios/Favoritos/actualizar_prioridad_favoritos.html',
                            {"formulario": formulario, "favorito": favorito})
            else:
                return mi_error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)

    return render(request, 'formularios/Favoritos/actualizar_prioridad_favoritos.html', {"formulario": formulario, "favorito": favorito})



#--------------------------------------Formularios DELETE-------------------------------------------------

def eliminar_producto(request, producto_id):
    # Vista para eliminar un producto en la API.

    try:
        headers = crear_cabecera()
        response = requests.delete(
            BASE_API_URL + version + 'productos/' + str(producto_id) + '/eliminar/',
            headers=headers,
        )

        if response.status_code == requests.codes.ok:
            mensaje = response.text.strip()
            messages.success(request, mensaje)
            return redirect("producto_listar_api")
        else:
            print(response.status_code)
            response.raise_for_status()
    except Exception as err:
        print(f'Ocurrió un error: {err}')
        return mi_error_500(request)

    return redirect('producto_listar_api')


def eliminar_orden(request, orden_id):
    # Vista para eliminar una orden y su archivo adjunto en la API.
    
    try:
        orden = helper.obtener_orden(orden_id)  # Obtiene los datos de la orden antes de eliminarla
        
        # Si la orden tiene un archivo adjunto, se elimina manualmente del almacenamiento
        if orden.get("archivo_adjunto"):
            ruta_archivo = os.path.join(BASE_DIR, "media", orden["archivo_adjunto"])
            if os.path.exists(ruta_archivo):
                os.remove(ruta_archivo)  # Elimina el archivo del sistema de archivos
                print(f"Archivo eliminado: {ruta_archivo}")

        headers = crear_cabecera()
        response = requests.delete(
            BASE_API_URL + version + 'ordenes/' + str(orden_id) + '/eliminar/',
            headers=headers,
        )

        if response.status_code == requests.codes.ok:
            mensaje = response.text.strip()
            messages.success(request, mensaje)
            return redirect("orden_listar_api")
        else:
            print(response.status_code)
            response.raise_for_status()
    
    except Exception as err:
        print(f'Ocurrió un error: {err}')
        return mi_error_500(request)

    return redirect('orden_listar_api')


def eliminar_proveedor(request, proveedor_id):
    """
    Vista para eliminar un proveedor en la API.
    """
    try:
        headers = crear_cabecera()
        response = requests.delete(
            BASE_API_URL + version + 'proveedores/' + str(proveedor_id) + '/eliminar/',
            headers=headers,
        )

        if response.status_code == requests.codes.ok:
            mensaje = response.text.strip()
            messages.success(request, mensaje)
            return redirect("proveedor_listar_api")
        else:
            print(response.status_code)
            response.raise_for_status()
    except Exception as err:
        print(f'Ocurrió un error: {err}')
        return mi_error_500(request)

    return redirect('proveedores_listar_api')

def eliminar_favoritos(request, favorito_id):
    try:
        headers = crear_cabecera()
        response = requests.delete(
            BASE_API_URL + version + 'favoritos/eliminar/' + str(favorito_id),
            headers=headers,
        )

        if response.status_code == requests.codes.ok:
            mensaje = response.text.strip()  # Extraer el mensaje de la API sin validaciones
            messages.success(request, mensaje)
            return redirect("favoritos_listar_api")
        else:
            print(response.status_code)
            response.raise_for_status()
    except Exception as err:
        print(f'Ocurrió un error: {err}')
        return mi_error_500(request)

    return redirect('favoritos_listar_api')

#--------------------------------------ViewSet-------------------------------------------------

def listar_productos_viewset(request):
    productos = helper.obtener_productos()  # Obtiene productos usando ViewSet
    return render(request, 'api/lista_productos_viewset.html', {"productos": productos})

def crear_producto_viewset(request):
    if request.method == "POST":
        try:
            formulario = ProductoForm(request.POST)
            datos = formulario.data.copy()

            response = helper.crear_producto(datos)  # Usar helper para llamar al ViewSet

            if response.status_code == 201:
                messages.success(request, "Producto creado exitosamente con ViewSet")
                return redirect("listar_productos_viewset")
            else:
                return render(request, "formularios/Producto/crear_producto.html", {"formulario": formulario})
        except Exception as err:
            print(f"Ocurrió un error: {err}")
            return render(request, "formularios/Producto/crear_producto.html", {"formulario": formulario})
    else:
        formulario = ProductoForm()
    return render(request, "formularios/Producto/crear_producto.html", {"formulario": formulario})

def editar_producto_viewset(request, producto_id):
    producto = helper.obtener_producto(producto_id)

    if request.method == "POST":
        formulario = ProductoForm(request.POST, initial=producto)

        if formulario.is_valid():
            datos = formulario.cleaned_data
            response = helper.editar_producto(producto_id, datos)

            if response.status_code == 200:
                messages.success(request, "Producto editado correctamente con ViewSet")
                return redirect("listar_productos_viewset")
    
    else:
        formulario = ProductoForm(initial=producto)

    return render(request, 'formularios/Producto/editar_producto.html', {"formulario": formulario, "producto": producto})

def actualizar_nombre_producto_viewset(request, producto_id):
    """
    Vista para actualizar solo el nombre de un producto usando ViewSet.
    """

    datosFormulario = None

    if request.method == "POST":
        datosFormulario = request.POST

    # 📌 Obtener el producto desde la API usando el helper
    producto = helper.obtener_producto(producto_id)

    formulario = ProductoActualizarNombreForm(datosFormulario,
        initial={
            'nombre': producto['nombre'],
        }
    )

    if request.method == "POST":
        try:
            formulario = ProductoActualizarNombreForm(request.POST)
            headers = crear_cabecera()
            datos = request.POST.copy()

            # 📌 Usar la URL del ViewSet en lugar de la tradicional
            response = requests.patch(
                f"{BASE_API_URL}{version}viewset/productos/{producto_id}/",
                headers=headers,
                data=json.dumps(datos)
            )

            if response.status_code == requests.codes.ok:
                return redirect("producto_listar_viewset_api")  # Redirige a la vista que usa ViewSet
            else:
                print(response.status_code)
                response.raise_for_status()

        except HTTPError as http_err:
            print(f'Hubo un error en la petición: {http_err}')

            if response.status_code == 400:
                errores = response.json()
                for error in errores:
                    formulario.add_error(error, errores[error])

                return render(request, 
                            'formularios/Producto/actualizar_nombre.html',
                            {"formulario": formulario, "producto": producto})
            else:
                return mi_error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)

    return render(request, 'formularios/Producto/actualizar_nombre.html', {"formulario": formulario, "producto": producto})


def eliminar_producto_viewset(request, producto_id):
    response = helper.eliminar_producto(producto_id)

    if response.status_code == 204:
        messages.success(request, "Producto eliminado correctamente con ViewSet")
    else:
        messages.error(request, "Error al eliminar producto con ViewSet")

    return redirect("listar_productos_viewset")


#------------------------------------------------usuario-----------------------------------------------------------------------------
#AGR12345
def registrar_usuario(request):
    if (request.method == "POST"):
        try:
            formulario = RegistroForm(request.POST)
            if(formulario.is_valid()):
                headers =  {
                            "Content-Type": "application/json" 
                        }
                response = requests.post(
                    BASE_API_URL + version + 'registrar/usuario/',
                    headers=headers,
                    data=json.dumps(formulario.cleaned_data)
                )
                
                if(response.status_code == requests.codes.ok):
                    usuario = response.json()
                    token_acceso = helper.obtener_token_session(
                            formulario.cleaned_data.get("username"),
                            formulario.cleaned_data.get("password1")
                            )
                    request.session["usuario"]=usuario
                    request.session["token"] = token_acceso
                    redirect("index")
                else:
                    print(response.status_code)
                    response.raise_for_status()
        except HTTPError as http_err:
            print(f'Hubo un error en la petición: {http_err}')
            if(response.status_code == 400):
                errores = response.json()
                for error in errores:
                    formulario.add_error(error,errores[error])
                return render(request, 
                            'registration/signup.html',
                            {"formulario":formulario})
            else:
                return mi_error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)
            
    else:
        formulario = RegistroForm()
    return render(request, 'registration/signup.html', {'formulario': formulario})

def login(request):
    if (request.method == "POST"):
        formulario = LoginForm(request.POST)
        try:
            token_acceso = helper.obtener_token_session(
                                formulario.data.get("usuario"),
                                formulario.data.get("password")
                                )
            request.session["token"] = token_acceso
            
            # Guardar token en la sesión de Django
            request.session["token"] = token_acceso

            if not token_acceso:
                print("❌ ERROR: No se recibió un token válido del servidor.")
                return render(request, 'registro/login.html', {"form": formulario, "error": "No se recibió un token válido."})

            print("🔑 Token recibido en login:", token_acceso)  # ✅ Verifica si el token es válido

            # 🔹 Guardar el token en el archivo .env
            env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
            set_key(env_path, "TOKEN_ACCESO", token_acceso)
            print("✅ Token guardado en .env correctamente")

          
            headers = {'Authorization': 'Bearer '+token_acceso} 
            response = requests.get(BASE_API_URL + version + 'usuario/token/' + token_acceso,headers=headers)
            usuario = response.json()
            request.session["usuario"] = usuario
            
            return  redirect("index")
        except Exception as excepcion:
            print(f'Hubo un error en la petición: {excepcion}')
            formulario.add_error("usuario",excepcion)
            formulario.add_error("password",excepcion)
            return render(request, 
                            'registro/login.html',
                            {"form":formulario})
    else:  
        formulario = LoginForm()
    return render(request, 'registro/login.html', {'form': formulario})

def logout(request):
    del request.session['token']
    return redirect('index')


# Páginas de error personalizadas
def mi_error_404(request, exception=None):
    return render(request, 'errores/404.html', None, None, 404)

def mi_error_500(request, exception=None):
    return render(request, 'errores/500.html', None, None, 500)