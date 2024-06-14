from .models import FrutaColor
from rest_framework import serializers

class FrutaColorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FrutaColor
        fields = ['id','fruta','color']

    def create(self,validated_data):
        #Crea un objeto de la clase Modelo(Worker)
        return FrutaColor.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        #actualiza una instancia con los validated_data
        instance.fruta = validated_data.get('fruta',instance.fruta)
        instance.color = validated_data.get('color',instance.color)
        instance.save()
        return instance

