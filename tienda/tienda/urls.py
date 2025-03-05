from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('productos/', producto_listar_api, name='producto_listar_api'), 
    path('productos/<int:id>/', producto_detalle_api, name='producto_detalle_api'),
    path('ordenes/', ordenes_listar_api, name='ordenes_listar_api'),
    path('proveedores/', proveedores_listar_api, name='proveedores_listar_api'),
    path('favoritos/', favoritos_listar_api, name='favoritos_listar_api'),
    path('usuarios/', usuario_listar_api, name='usuarios_listar_api'),


    
    #busquedas avanzadas
    path('busqueda-productos-simple/', producto_busqueda_simple, name='producto_busqueda_simple'),
    path('busqueda-productos-avanzada/', producto_busqueda_avanzada, name='producto_busqueda_avanzada'),
    path('busqueda-ordenes/', orden_busqueda_avanzada, name='orden_busqueda_avanzada'),
    path('busqueda-proveedores/', proveedor_busqueda_avanzada, name='proveedor_busqueda_avanzada'),
    
    # POST
    path('productos/crear/', crear_producto, name='producto_crear_api'),
    path('ordenes/crear/', crear_orden, name='orden_crear_api'),
    path('proveedores/crear/', crear_proveedor, name='proveedor_crear_api'),
    path('favoritos/crear/', crear_favorito, name='favoritos_crear_api'),
    path('usuarios/crear/', crear_usuario, name='crear_usuario'),

    
    # PUT
    path('productos/<int:producto_id>/editar/', editar_producto, name='producto_editar_api'),
    path('ordenes/<int:orden_id>/editar/', editar_orden, name='orden_editar_api'),
    path('proveedores/<int:proveedor_id>/editar/', editar_proveedor, name='proveedor_editar_api'),
    path('favoritos/<int:favorito_id>/editar/', editar_favoritos, name='editar_favoritos_api'),

    # PATCH
    path('productos/<int:producto_id>/actualizar-nombre/', actualizar_nombre_producto, name='producto_actualizar_nombre_api'),
    path('ordenes/<int:orden_id>/actualizar-estado/', actualizar_estado_orden, name='orden_actualizar_estado_api'),
    path('proveedores/<int:proveedor_id>/actualizar-contacto/', actualizar_contacto_proveedor, name='proveedor_actualizar_contacto_api'),
    path('favoritos/<int:favorito_id>/actualizar-prioridad/', actualizar_prioridad_favoritos, name='actualizar_prioridad_favoritos_api'),
    
    # DELETE
    path('productos/<int:producto_id>/eliminar/', eliminar_producto, name='producto_eliminar_api'),
    path('ordenes/<int:orden_id>/eliminar/', eliminar_orden, name='orden_eliminar_api'),
    path('proveedores/<int:proveedor_id>/eliminar/', eliminar_proveedor, name='proveedor_eliminar_api'),
    path('favoritos/<int:favorito_id>/eliminar/', eliminar_favoritos, name='eliminar_favoritos_api'),


    #OBTENER
    path('producto/<int:producto_id>/', obtener_producto, name='obtener_producto'),
    path('orden/<int:orden_id>/', obtener_orden, name='obtener_orden'),
    path('proveedor/<int:proveedor_id>/', obtener_proveedor, name='obtener_proveedor'),
    path('favoritos/<int:favorito_id>/', obtener_favoritos, name='obtener_favoritos'),
    
    
    #ViewSet
    path('productos-viewset/', listar_productos_viewset, name="listar_productos_viewset"),
    path('productos-viewset/crear/', crear_producto_viewset, name="crear_producto_viewset"),
    path('productos-viewset/<int:producto_id>/editar/', editar_producto_viewset, name="editar_producto_viewset"),
    path('productos/<int:producto_id>/actualizar-nombre-viewset/', actualizar_nombre_producto_viewset, name='producto_actualizar_nombre_viewset_api'),
    path('productos-viewset/<int:producto_id>/eliminar/', eliminar_producto_viewset, name="eliminar_producto_viewset"),

    
    #Usuario
    path('registrar', registrar_usuario,name='registrar_usuario'),
    path('login', login,name='login'),
    path('logout', logout,name='logout'),
    
    
    #GET autentificacion
    path('mis-ordenes/', listar_orden_usuario, name='listar_orden_usuario'),
    path('mis-favoritos/', listar_favoritos_usuario, name='listar_favoritos_usuario'),
    
    
    #POST autentificacion
    path('crear-orden/', crear_orden_usuario, name='crear_orden_usuario'),
    path('crear-favorito/', crear_favorito_usuario, name='crear_favorito_usuario'),

]