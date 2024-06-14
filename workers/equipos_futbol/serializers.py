from .models import EquipoFutbol
from rest_framework import serializers

class EquipoFutbolSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EquipoFutbol
        fields = ['id','equipo']


    def create(self,validated_data):
        #Crea un objeto de la clase Modelo(Worker)
        return EquipoFutbol.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        #actualiza una instancia con los validated_data
        instance.equipo = validated_data.get('equipo',instance.equipo)
        instance.save()
        return instance