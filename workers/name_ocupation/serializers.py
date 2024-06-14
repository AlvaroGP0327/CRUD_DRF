from .models import Worker,JobSite
from rest_framework import serializers

#FORMA #1 IIMPLEMENTANDO models y serializers class
class WorkerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False,allow_blank=True,max_length=100)
    ocupation = serializers.CharField(required=False,allow_blank=True,max_length=100)

    #Se crean los metodos para implementar el CRUD

#Serializacion: convertir Objetos django complejos a diccionarios
#Deserializacion: convertir JSON a diccionarios

    #Metodos para definir el comportamiento
    #cuando se llame a serializer.save()
    
    def create(self,validated_data):
        #Crea un objeto de la clase Modelo(Worker)
        return Worker.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        #actualiza una instancia con los validated_data
        instance.name = validated_data.get('name',instance.name)
        instance.ocupation = validated_data.get('ocupation',instance.ocupation)
        instance.save()
        return instance

#Implementacion de ModelSerializer
#Evita repetir codigo en la parte de atributos
#Es un atajo para crear las clases del serializer
class JobSiteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobSite
        fields = ['id','city','company']


    def create(self,validated_data):
        #Crea un objeto de la clase Modelo(Worker)
        return JobSite.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        #actualiza una instancia con los validated_data
        instance.city = validated_data.get('city',instance.city)
        instance.company = validated_data.get('company',instance.company)
        instance.save()
        return instance
