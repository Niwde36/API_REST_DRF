# models: Se importa desde django.db y proporciona  las herramientas 
# necesarias para definir campos y comportamientos de los modelos:

from django.db import models

# Aquí se crean los modelos
# Car: Es el nombre de la clase que define el modelo. En este caso, representa 
# un carro.
# models.Model: La clase base para todos los modelos de Django. Al heredar de 
# models.Model, Car se convierte en un modelo Django que se mapea a una tabla 
# en la base de datos.

class Car(models.Model):

    # marca es un atributo de la clase Car, que corresponde a una columna
    # en la base de datos, usando models.Charfield que es un tipo de campo
    # para almacenar cadenas de texto y tiene definida una longitud máxima de 100
    # caracteres:

    brand = models.CharField(max_length=100)


    # __str__: Es un método especial en Python que define cómo se debe 
    # representar el modelo como una cadena de texto. En este caso, devuelve 
    # la marca del carro:

    def __str__(self):
        return self.brand