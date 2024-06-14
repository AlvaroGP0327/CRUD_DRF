Este proyecto de CRUD que esta construido con Django
y DRF.Consta de 4 aplicaciones en las que en cada
una de ellas se realiza una implementacion distinta
para construir las vistas.
El objetivo es tener una referencia de la sintaxis y la implementacion
Los serializers se construyen extendiendo desde la misma
clase madre.Teniendo la posibilidad de modificar sus metodos.
Cada aplicacion se construyeron las vistas implementando diferentes
conceptos.
las vistas las cuales se pueden implementar de diferentes formas.
    1-Vistas basadas en funciones:(name_ocupation),se construyen
    decorando la funcion con @api_view.
    2-Vistas basadas en clases:(capitales), se construyen heredando
    desde la clase APIView, se deben construir dos clases una para get
    y post, y otra para los demas metodos.
    3- Vistas genericas(equipos_futbol), se construyen heredando desde genericas
    solo se necesita el queryset y el serializers.
    4- Vistas genericas y mixins(fruta_color), sirven para editar los metodos y extenderlos
    a partir de una vista generica.
