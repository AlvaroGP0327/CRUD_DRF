from django.urls import path
from capitales import views
from rest_framework.urlpatterns import format_suffix_patterns

#Enlazar la ruta con la vista
urlpatterns = [
    path('capitales_list/',views.CapitalList.as_view()),
    path('capitales_details/<int:id>',views.CapitalDetails.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
