from django.urls import path
from fruta_color import views
from rest_framework.urlpatterns import format_suffix_patterns

#Enlazar la ruta con la vista
urlpatterns = [
    path('fruta_color_list/',views.FrutaColorList.as_view()),
    path('fruta_color_details/<int:id>/',views.FrutaColorDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
