from django.urls import path
from .views import (
    index, producto_listar_api, producto_detalle_api, 
    ordenes_listar_api, proveedores_listar_api, 
    producto_busqueda_avanzada, login_view, 
    orden_busqueda_avanzada, proveedor_busqueda_avanzada, producto_busqueda_simple
)

urlpatterns = [
    path('', index, name='index'),
    path("login/", login_view, name="login"),
    path('productos/', producto_listar_api, name='producto_listar_api'), 
    path('productos/<int:id>/', producto_detalle_api, name='producto_detalle_api'),
    path('ordenes/', ordenes_listar_api, name='ordenes_listar_api'),
    path('proveedores/', proveedores_listar_api, name='proveedores_listar_api'),
    
    #busquedas avanzadas
    path('busqueda-productos-simple/', producto_busqueda_simple, name='producto_busqueda_simple'),
    path('busqueda-productos-avanzada/', producto_busqueda_avanzada, name='producto_busqueda_avanzada'),
    path('busqueda-ordenes/', orden_busqueda_avanzada, name='orden_busqueda_avanzada'),
    path('busqueda-proveedores/', proveedor_busqueda_avanzada, name='proveedor_busqueda_avanzada'),
]