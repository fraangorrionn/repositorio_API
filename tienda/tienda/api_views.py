from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework import status

@api_view(['GET'])
def orden_list(request):
    ordenes = Orden.objects.all()
    #serializer = LibroSerializer(libros, many=True)
    serializer = OrdenSerializer(ordenes, many=True)
    return Response(serializer.data)