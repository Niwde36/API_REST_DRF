# El serializador se usa para transformar datos nativos de python como diccionarios 
# en datos que se pueden enviar o recibir a través de una API como JSON.

# serializers se importa desde rest_framework y proporciona las clases y métodos
# necesarios para definir y manejar serializadores.
from rest_framework import serializers

# Aquí se importa la clase Car desde models.py
from myapp.models import Car


# serializers.ModelSerializer: Es una clase proporcionada por DRF que simplifica
# la creación de un serializador para un modelo Django. Automáticamente genera 
# campos basados en el modelo y maneja la conversión entre datos del modelo y datos
# JSON.
class CarSerializer(serializers.ModelSerializer):

    # class Meta: Es una clase interna en el serializador que se usa para 
    # proporcionar metainformación sobre el serializador.

    class Meta:
        # Aquí indico que este serializador está asociado al modelo CAr
        model = Car
        # Especifica que campos del modelo deben incluirse en la representación
        # del serializador.
        fields = ['id', 'brand']
