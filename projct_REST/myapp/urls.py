# Acá se definen las rutas específicas para las vistas de la app

# path se importa para definir rutas en Django
from django.urls import path
#Acá importo las vistas que están en views.py
from .views import CarListCreate, CarDetail

urlpatterns = [
    # Ruta para solicitudes GET y POST
    path('cars/', CarListCreate.as_view(), name='car-list-create'),
    # Ruta para solicitudes GET, PUT/PATCH y DELETE
    path('cars/<int:pk>/', CarDetail.as_view(), name='car-detail'),
]
