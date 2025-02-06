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
        self.access_token = self.request.session.get("access_token", None)
        self.refresh_token = self.request.session.get("refresh_token", None)

        self.headers = {
            'Authorization': f'Bearer {self.access_token}' if self.access_token else '',
            "Content-Type": "application/json"
        }

        print(f"🔍 Token enviado en headers: {self.headers['Authorization']}")
    
    def _actualizar_token(self):
        """
        Intenta refrescar el token si es inválido.
        """
        if not self.refresh_token:
            print("⚠️ No hay refresh token disponible")
            return False  # No se puede refrescar

        url = "http://127.0.0.1:8000/api/v1/token/refresh/"
        response = requests.post(url, data={"refresh": self.refresh_token})

        if response.status_code == 200:
            new_tokens = response.json()
            self.access_token = new_tokens["access"]
            self.request.session["access_token"] = self.access_token
            self.headers["Authorization"] = f"Bearer {self.access_token}"
            print("✅ Token refrescado correctamente")
            return True
        else:
            print("❌ Error al refrescar el token:", response.json())
            return False

    def _realizar_peticion(self, url, params=None):
        """
        Realiza una petición GET con autenticación.
        """
        response = requests.get(url, headers=self.headers, params=params)

        if response.status_code == 401:  # Token inválido, intenta refrescarlo
            print("⚠️ Token expirado. Intentando refrescar...")
            if self._actualizar_token():
                response = requests.get(url, headers=self.headers, params=params)  # Reintenta la petición

        return response.json() if response.status_code == 200 else []

    def obtener_productos(self, params=None):
        """
        Obtiene la lista de productos desde la API REST.
        """
        url = 'http://127.0.0.1:8000/api/v1/productos/busqueda-avanzada/'
        return self._realizar_peticion(url, params)

    def obtener_ordenes(self, params=None):
        """
        Obtiene la lista de órdenes desde la API REST.
        """
        url = 'http://127.0.0.1:8000/api/v1/ordenes/busqueda-avanzada/'
        return self._realizar_peticion(url, params)

    def obtener_proveedores(self, params=None):
        """
        Obtiene la lista de proveedores desde la API REST.
        """
        url = 'http://127.0.0.1:8000/api/v1/proveedores/busqueda-avanzada/'
        return self._realizar_peticion(url, params)
