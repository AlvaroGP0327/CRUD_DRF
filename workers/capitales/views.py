'''APIView vistas basadas en clases:
Una clase que hereda de otra proveniente
de un framework que tiene metodos que manejan
diferentes tipos de solicitudes(GET POST...etc)'''

'''Se utilizan clases que usan los modelos
y los serializers para construir las consultas
a la base de datos (querysets)'''

from .models import Capitales
from .serializers import CapitalesSerializer
from django.http import Http404
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
#Vistas basadas en clases
class CapitalList(APIView):
    """metodos para traer todos los registros,
    o crear un nuevo registro"""
    def get(self,request,format=None):
        capitales = Capitales.objects.all()
        serializer = CapitalesSerializer(capitales,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = CapitalesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CapitalDetails(APIView):
    '''Consultar, modificar o borrar un solo
    objeto de la base de datos'''

    def get_object(self,id):
        #Trae un objeto de la db si existe
        try:
            return Capitales.objects.get(id=id)
        except Capitales.DoesNotExist:
            raise Http404
        
    def get(self,request,id,format=None):
        #Trae objeto de db, lo serializa y retorna JSON
        capital = self.get_object(id)
        serializer = CapitalesSerializer(capital)
        return Response(serializer.data)
    
    def put(self,request,id,format=None):
        #Traer objeto de db para modificar
        capital = self.get_object(id)
        #Asignar la data del request a el objeto serializado
        serializer = CapitalesSerializer(capital,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id,format=None):
        capital = self.get_object(id)
        capital.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)