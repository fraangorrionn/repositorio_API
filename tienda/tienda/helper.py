import requests
import environ
import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'), True)
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
        headers = {'Authorization': 'Bearer '+env("Admin")}
        response = requests.get(BASE_API_URL + version + 'usuarios/', headers=headers)
        usuarios = response.json()

        # Arma una lista de tuplas (id, nombre) para poner en el formulario
        lista_usuarios = []
        for usuario in usuarios:
            lista_usuarios.append((usuario["id"], usuario["username"]))
        return lista_usuarios

    def obtener_favoritos():
        headers = {'Authorization': 'Bearer ' + env("Admin")}
        response = requests.get(BASE_API_URL + version + 'favoritos/', headers=headers)
        favoritos = response.json()
        return favoritos

    def obtener_favorito(id):
        headers = {'Authorization': 'Bearer ' + env("Admin")}
        response = requests.get(BASE_API_URL + version + f'favoritos/{id}', headers=headers)
        favorito = response.json()
        return favorito