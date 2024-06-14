from django.urls import path
from name_ocupation import views
from rest_framework.urlpatterns import format_suffix_patterns

#Enlazar la ruta con la vista
urlpatterns = [
    path('workers_list/', views.worker_list),
    path('worker_detail/<int:id>/',views.worker_details),
]
urlpatterns = format_suffix_patterns(urlpatterns)

