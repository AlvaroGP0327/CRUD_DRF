'''@api_view funciones basadas en vistas:
Se implementan decoradores(wrappers) para
manejar las vistas (APIViews)
toma una solicitud (request) y devuelve
una respuesta (response).
APIView vistas basadas en clases:
Una clase que hereda de otra proveniente
del framework que tiene metodos que manejan
diferentes tipos de solicitudes(GET POST...etc)'''
'''Se utilizan clases que usan los modelos
y los serializers para construir las consultas
a la base de datos (querysets)'''

from .models import Worker,JobSite
from .serializers import WorkerSerializer, JobSiteSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
#Implementacion del CRUD
@api_view(['GET','POST'])
def worker_list(request, format=None):
    '''Lista todos los trabajadores
    o permite ingresar uno nuevo'''
    if request.method == 'GET':
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        #deserializar
        serializer = WorkerSerializer(data=request.data)
        #validar datos ingresados
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #Si validated False
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def worker_details(request,id,format=None):
    #Traer recurso de la base de datos
    #Para procesar via put o delete
    try:
        #Trae el recurso especifico solicitado por id
        worker = Worker.objects.get(id=id)
    except Worker.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = WorkerSerializer(worker)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        #convertir el JSON a objeto worker
        #Relacionar objeto con la data para hacer el PUT
        serializer = WorkerSerializer(worker,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        worker.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


