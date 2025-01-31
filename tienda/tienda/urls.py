from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('api/', views.producto_listar_api, name='producto_listar_api'),
    path('api/', views.producto_detalle_api, name='producto_detalle_api'),
]