from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('productos/', producto_listar_api, name='producto_listar_api'), 
    path('productos/<int:id>/', producto_detalle_api, name='producto_detalle_api'),
    path('ordenes/', ordenes_listar_api, name='ordenes_listar_api'),
    path('proveedores/', proveedores_listar_api, name='proveedores_listar_api'),
    
    #busquedas avanzadas
    path('busqueda-productos-simple/', producto_busqueda_simple, name='producto_busqueda_simple'),
    path('busqueda-productos-avanzada/', producto_busqueda_avanzada, name='producto_busqueda_avanzada'),
    path('busqueda-ordenes/', orden_busqueda_avanzada, name='orden_busqueda_avanzada'),
    path('busqueda-proveedores/', proveedor_busqueda_avanzada, name='proveedor_busqueda_avanzada'),
    
    # POST
    path('productos/crear/', crear_producto, name='producto_crear_api'),
    
    # PUT
    path('productos/<int:producto_id>/editar/', editar_producto, name='producto_editar_api'),

    # PATCH
    path('productos/<int:producto_id>/actualizar-nombre/', actualizar_nombre_producto, name='producto_actualizar_nombre_api'),
    
    # DELETE
    path('productos/<int:producto_id>/eliminar/', eliminar_producto, name='producto_eliminar_api'),
]