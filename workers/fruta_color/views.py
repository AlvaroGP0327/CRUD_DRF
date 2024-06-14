'''Implementacion de mixins y generics
para abstraer los metodos para realizar el CRUD'''
'''Los mixins sirven para editar la logica de las
vistas genericas.'''
'''Se declaran dos clases una para GET y POST,
y la otra PUT, UPDATE, DELETE.'''
'''Esta implementacion tiene un alto nivel
de abstraccion
'''

from .models import FrutaColor
from .serializers import FrutaColorSerializer
from rest_framework import mixins, generics
# Create your views here.
#La vista extiende desde mixins y generics.
#esto para crear la vista generica y ademas
#tener la posibilidad de editar la logica.
class FrutaColorList(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     generics.GenericAPIView):
    
    #Clase para manejar GET y POST
    queryset = FrutaColor.objects.all()
    serializer_class = FrutaColorSerializer

    def get(self,request,*arg,**kwargs):
        return self.list(request, *arg, **kwargs)

    def post(self,request,*arg,**kwargs):
        return self.create(request, *arg,**kwargs)

class FrutaColorDetails(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
        
        #Clase para manejar GET PUT DELETE
        queryset = FrutaColor.objects.all()
        serializer_class = FrutaColorSerializer
        lookup_field = 'id'
        
        def get(self, request, *args, **kwargs):
            return self.retrieve(request, *args, **kwargs)

        def put(self, request, *args, **kwargs):
            return self.update(request, *args, **kwargs)

        def delete(self, request, *args, **kwargs):
            return self.destroy(request, *args, **kwargs)


