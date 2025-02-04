import requests
import environ
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'), True)
env = environ.Env()


class Helper:
    """
    Clase Helper para manejar la conexión con la API REST.
    """

    def __init__(self, request):
        """
        Inicializa la clase con la solicitud del usuario.
        """
        self.request = request
        self.headers = {
            'Authorization': f'Bearer {self.request.session.get("access_token", "")}',
            "Content-Type": "application/json"
        }

    def obtener_productos(self, params=None):
        """
        Obtiene la lista de productos desde la API REST.
        """
        url = 'http://127.0.0.1:8000/api/productos/busqueda-avanzada/'
        response = requests.get(url, headers=self.headers, params=params)
        return response.json() if response.status_code == 200 else []

    def obtener_ordenes(self, params=None):
        """
        Obtiene la lista de órdenes desde la API REST.
        """
        url = 'http://127.0.0.1:8000/api/ordenes/busqueda-avanzada/'
        response = requests.get(url, headers=self.headers, params=params)
        return response.json() if response.status_code == 200 else []

    def obtener_proveedores(self, params=None):
        """
        Obtiene la lista de proveedores desde la API REST.
        """
        url = 'http://127.0.0.1:8000/api/proveedores/busqueda-avanzada/'
        response = requests.get(url, headers=self.headers, params=params)
        return response.json() if response.status_code == 200 else []
