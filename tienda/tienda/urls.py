from django.urls import path
from django.urls import path, include
from .views import index, producto_listar_api, producto_detalle_api, ordenes_listar_api, proveedores_listar_api,busqueda_avanzada_producto_view
from django.contrib.auth import views as auth_views

from .views import busqueda_avanzada_producto_view

urlpatterns = [
    path('', index, name='index'),
    path('productos/', producto_listar_api, name='producto_listar_api'), 
    path('productos/<int:id>/', producto_detalle_api, name='producto_detalle_api'),
    path('ordenes/', ordenes_listar_api, name='ordenes_listar_api'),
    path('proveedores/', proveedores_listar_api, name='proveedores_listar_api'),
    path('busqueda-productos/', busqueda_avanzada_producto_view, name='busqueda_avanzada_producto_view'),
]
