from django.shortcuts import render

# Aquí defino las vistas que manejan las solicitudes HTTP para la API.
# En este caso son vistas genéricas proporcionadas por DRF para operaciones CRUD

from rest_framework import generics
from .models import Car
from .serializers import CarSerializer

# Vista para gestionar POST y GET
class CarListCreate(generics.ListCreateAPIView):
    # Define el conjunto de datos que se van a usar, en este caso todos de los
    # datos de los objetos Car
    queryset = Car.objects.all()
    # Aquí defino el serializador que se usará para transformar datos
    serializer_class = CarSerializer

#Vista para gestionar GET PUT y DELETE
class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    # Defino conjunto de datos
    queryset = Car.objects.all()
    # Defino serializador que se usará
    serializer_class = CarSerializer


#*****************************************************************************

# Funcionalidad de las Vistas

# CarListCreate:

# GET /api/cars/: Devuelve una lista de todos los coches en formato JSON.
# POST /api/cars/: Permite crear un nuevo coche. Los datos del coche deben 
# ser enviados en el cuerpo de la solicitud en formato JSON.

# CarDetail:

# GET /api/cars/<id>/: Devuelve los detalles del coche con el ID especificado.
# PUT/PATCH /api/cars/<id>/: Actualiza el coche con el ID especificado. Los datos 
# actualizados deben ser enviados en el cuerpo de la solicitud en formato JSON.
# DELETE /api/cars/<id>/: Elimina el coche con el ID especificado.

#****************************************************************************