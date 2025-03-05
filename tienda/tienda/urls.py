from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.producto_listar_api, name='producto_listar_api'), 
    path('productos/<int:id>/', views.producto_detalle_api, name='producto_detalle_api'),
    path('ordenes/', views.ordenes_listar_api, name='ordenes_listar_api'),
    path('proveedores/', views.proveedores_listar_api, name='proveedores_listar_api'),
    path('favoritos/', views.favoritos_listar_api, name='favoritos_listar_api'),
    path('usuarios/', views.usuario_listar_api, name='usuarios_listar_api'),


    
    #busquedas avanzadas
    path('busqueda-productos-simple/', views.producto_busqueda_simple, name='producto_busqueda_simple'),
    path('busqueda-productos-avanzada/', views.producto_busqueda_avanzada, name='producto_busqueda_avanzada'),
    path('busqueda-ordenes/', views.orden_busqueda_avanzada, name='orden_busqueda_avanzada'),
    path('busqueda-proveedores/', views.proveedor_busqueda_avanzada, name='proveedor_busqueda_avanzada'),
    
    # POST
    path('productos/crear/', views.crear_producto, name='producto_crear_api'),
    path('ordenes/crear/', views.crear_orden, name='orden_crear_api'),
    path('proveedores/crear/', views.crear_proveedor, name='proveedor_crear_api'),
    path('favoritos/crear/', views.crear_favorito, name='favoritos_crear_api'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),

    
    # PUT
    path('productos/<int:producto_id>/editar/', views.editar_producto, name='producto_editar_api'),
    path('ordenes/<int:orden_id>/editar/', views.editar_orden, name='orden_editar_api'),
    path('proveedores/<int:proveedor_id>/editar/', views.editar_proveedor, name='proveedor_editar_api'),
    path('favoritos/<int:favorito_id>/editar/', views.editar_favoritos, name='editar_favoritos_api'),

    # PATCH
    path('productos/<int:producto_id>/actualizar-nombre/', views.actualizar_nombre_producto, name='producto_actualizar_nombre_api'),
    path('ordenes/<int:orden_id>/actualizar-estado/', views.actualizar_estado_orden, name='orden_actualizar_estado_api'),
    path('proveedores/<int:proveedor_id>/actualizar-contacto/', views.actualizar_contacto_proveedor, name='proveedor_actualizar_contacto_api'),
    path('favoritos/<int:favorito_id>/actualizar-prioridad/', views.actualizar_prioridad_favoritos, name='actualizar_prioridad_favoritos_api'),
    
    # DELETE
    path('productos/<int:producto_id>/eliminar/', views.eliminar_producto, name='producto_eliminar_api'),
    path('ordenes/<int:orden_id>/eliminar/', views.eliminar_orden, name='orden_eliminar_api'),
    path('proveedores/<int:proveedor_id>/eliminar/', views.eliminar_proveedor, name='proveedor_eliminar_api'),
    path('favoritos/<int:favorito_id>/eliminar/', views.eliminar_favoritos, name='eliminar_favoritos_api'),


    #OBTENER
    path('producto/<int:producto_id>/', views.obtener_producto, name='obtener_producto'),
    path('orden/<int:orden_id>/', views.obtener_orden, name='obtener_orden'),
    path('proveedor/<int:proveedor_id>/', views.obtener_proveedor, name='obtener_proveedor'),
    path('favoritos/<int:favorito_id>/', views.obtener_favoritos, name='obtener_favoritos'),
    
    
    #ViewSet
    path('productos-viewset/', views.listar_productos_viewset, name="listar_productos_viewset"),
    path('productos-viewset/crear/', views.crear_producto_viewset, name="crear_producto_viewset"),
    path('productos-viewset/<int:producto_id>/editar/', views.editar_producto_viewset, name="editar_producto_viewset"),
    path('productos/<int:producto_id>/actualizar-nombre-viewset/', views.actualizar_nombre_producto_viewset, name='producto_actualizar_nombre_viewset_api'),
    path('productos-viewset/<int:producto_id>/eliminar/', views.eliminar_producto_viewset, name="eliminar_producto_viewset"),

    
    #Usuario
    path('registrar', views.registrar_usuario,name='registrar'),
    path('login', views.login,name='login'),
    path('logout', views.logout,name='logout'),
    
    
    #GET autentificacion
    path('mis-ordenes/', views.listar_orden_usuario, name='listar_orden_usuario'),
    path('mis-favoritos/', views.listar_favoritos_usuario, name='listar_favoritos_usuario'),
    
    
    #POST autentificacion
    path('crear-orden/', views.crear_orden_usuario, name='crear_orden_usuario'),
    path('crear-favorito/', views.crear_favorito_usuario, name='crear_favorito_usuario'),

]