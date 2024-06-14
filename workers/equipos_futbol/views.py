
from .models import EquipoFutbol
from .serializers import EquipoFutbolSerializer
from rest_framework import generics

# Create your views here.
#Vistas genericas esta es la abstraccion mas grande
#Abstrae la parte de tener que construir y validar
#el serializer con la data que se recibe
#Solo hay que definir los dos atributos
class EquipoFutbolList(generics.ListCreateAPIView):
    queryset = EquipoFutbol.objects.all()
    serializer_class = EquipoFutbolSerializer
    
class EquipoFutbolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EquipoFutbol.objects.all()
    serializer_class = EquipoFutbolSerializer
    lookup_field = 'id'

