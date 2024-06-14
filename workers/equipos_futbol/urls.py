from django.urls import path
from equipos_futbol import views
from rest_framework.urlpatterns import format_suffix_patterns

#Enlazar la ruta con la vista
urlpatterns = [
    path('equipos_list/',views.EquipoFutbolList.as_view()),
    path('equipos_details/<int:id>/',views.EquipoFutbolDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
