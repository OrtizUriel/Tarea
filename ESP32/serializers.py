# ----------------librerias------------
from rest_framework import routers, serializers, viewsets

# ----------------Modelos--------------
# Nombre app                      nombre modelo
from ESP32.models import ESP32
from drf_dynamic_fields import DynamicFieldsMixin
#                         serializers
class ESP32Serializers(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = ESP32
        fields = ('id','id_user','num_esp32','mac_esp32','delete','date_now')

