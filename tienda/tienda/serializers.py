from rest_framework import serializers
from .models import *
                
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        
class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'
        
class DetalleOrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleOrden
        fields = '__all__'
        
class ProvedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provedor
        fields = '__all__'
        
class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = '__all__'
        
class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = '__all__'
        
class FavoritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favoritos
        fields = '__all__'
        
class ReclamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reclamo
        fields = '__all__'
        
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        
class ProductoCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoCategoria
        fields = '__all__'
