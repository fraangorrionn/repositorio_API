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
