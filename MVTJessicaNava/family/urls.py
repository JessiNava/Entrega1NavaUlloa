from django.urls import path

from family import views


urlpatterns = [
   
    path('', views.inicio, name="inicio"),
    path('family', views.familia, name="familia"),
    path('hobbies', views.hobbies, name="hobbies"),
    path('ubicacion', views.ubicacion, name="ubicacion"),
    path('busquedafamilia', views.busquedafamilia, name="busquedafamilia"),
    path('hobbieformulario', views.hobbieformulario, name="hobbieformulario"),
    path('buscar/', views.buscar),
   
]

