# ----------------librerias------------
from rest_framework import routers, serializers, viewsets

# ----------------Modelos--------------
from Profesor.models import Profesor

from drf_dynamic_fields import DynamicFieldsMixin

class ProfesorSerializers(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ('id','address','name','ap_pat','ap_mat','telefono','edad','sexo','yearsExperience','fechaNacimiento')

