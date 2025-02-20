import requests
import environ
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'),True)
env = environ.Env()

BASE_API_URL = env("BASE_API_URL")
version = env("version")

class helper:

    def obtener_productos():
        # Obtiene todos los productos desde la API

        headers = {'Authorization': 'Bearer ' + env("Admin")} 
        response = requests.get(BASE_API_URL + version + 'productos/', headers=headers)
        productos = response.json()

        lista_productos = []
        for producto in productos:
            lista_productos.append((producto["id"], producto["nombre"]))
        return lista_productos

    def obtener_producto(id):
        # Obtiene un producto específico por su ID
        
        headers = {'Authorization': 'Bearer ' + env("Admin")} 
        response = requests.get(BASE_API_URL + version + 'productos/' + str(id), headers=headers)
        producto = response.json()
        return producto

    def obtener_orden(id):
        # Obtiene una orden específica por su ID desde la API.
        
        headers = {'Authorization': 'Bearer ' + env("Admin")} 
        response = requests.get(BASE_API_URL + version + 'ordenes/' + str(id), headers=headers)
        orden = response.json()
        return orden
    
    def obtener_proveedor(id):
        # Obtiene un proveedor específico por su ID desde la API.
        headers = {'Authorization': 'Bearer ' + env("Admin")} 
        response = requests.get(BASE_API_URL + version + 'proveedores/' + str(id), headers=headers)
        proveedor = response.json()
        return proveedor


    def obtener_usuarios():
        headers = {'Authorization': f'Bearer {env("Admin")}'}
        response = requests.get(f"{BASE_API_URL}/usuarios/", headers=headers)

        print("🔍 API Response Status:", response.status_code)
        print("🔍 API Response Content:", response.text)  # 👈 Esto nos mostrará la respuesta real

        if response.status_code == 200:
            try:
                usuarios_json = response.json()  # Intentar parsear JSON
                print("JSON recibido:", usuarios_json)  # Verificar si los datos están bien estructurados
                return [(usuario["id"], usuario["username"]) for usuario in usuarios_json]
            except requests.JSONDecodeError:
                print("❌ Error: La respuesta de la API no es un JSON válido")
                return []
        else:
            print(f"❌ Error al obtener usuarios: {response.status_code}")
            return []


    def obtener_productos():
        headers = {'Authorization': 'Bearer '+env("Admin")}
        response = requests.get(BASE_API_URL + version + 'productos/', headers=headers)
        productos = response.json()

        lista_productos = []
        for producto in productos:
            lista_productos.append((producto["id"], producto["nombre"]))
        return lista_productos

    def obtener_favoritos():
        headers = {'Authorization': 'Bearer ' + env("Admin")}
        response = requests.get(BASE_API_URL + version + 'favoritos/', headers=headers)
        favoritos = response.json()
        return favoritos
    
    def obtener_favorito(id):
        headers = {'Authorization': 'Bearer ' + env("Admin")}
        response = requests.get(BASE_API_URL + version + f'favoritos/{id}/', headers=headers)
        favorito = response.json()
        return favorito 

    #ViewSet
    
    '''He agregado @staticmethod para los metodos que no necesitan acceder a self ni a cls, 
    aquellos que no dependen del estado del objeto ni de la clase'''
    @staticmethod
    def obtener_productos():
        headers = {'Authorization': f'Bearer {env("Admin")}'}
        response = requests.get(f"{BASE_API_URL}/api/v1/productos-viewset/", headers=headers)
        return response.json() if response.status_code == 200 else []

    @staticmethod
    def obtener_producto(producto_id):
        headers = {'Authorization': f'Bearer {env("Admin")}'}
        response = requests.get(f"{BASE_API_URL}/api/v1/productos-viewset/{producto_id}/", headers=headers)
        return response.json() if response.status_code == 200 else {}

    @staticmethod
    def crear_producto(datos):
        headers = {'Authorization': f'Bearer {env("Admin")}', "Content-Type": "application/json"}
        return requests.post(f"{BASE_API_URL}/api/v1/productos-viewset/", headers=headers, data=json.dumps(datos))

    @staticmethod
    def editar_producto(producto_id, datos):
        headers = {'Authorization': f'Bearer {env("Admin")}', "Content-Type": "application/json"}
        return requests.put(f"{BASE_API_URL}/api/v1/productos-viewset/{producto_id}/", headers=headers, data=json.dumps(datos))

    @staticmethod
    def eliminar_producto(producto_id):
        headers = {'Authorization': f'Bearer {env("Admin")}'}
        return requests.delete(f"{BASE_API_URL}/api/v1/productos-viewset/{producto_id}/", headers=headers)
