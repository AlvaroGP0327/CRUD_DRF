from .models import Capitales
from rest_framework import serializers

class CapitalesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Capitales
        fields = ['id','country','capital']


    '''En esta implementacion se hace la reescritura de los metodos
    que vienen con la clase serializer.Esto es util si queremos agregar
    alguna logica adicional para modificar los datos antes de guardar
    la instancia en la base de datos.
    Esta implementacion fue tomada de la documentacion de DRF'''

    def create(self,validated_data):
        #Crea un objeto de la clase Modelo(Worker)
        return Capitales.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        #actualiza una instancia con los validated_data
        instance.country = validated_data.get('country',instance.country)
        instance.capital = validated_data.get('capital',instance.capital)
        instance.save()
        return instance

