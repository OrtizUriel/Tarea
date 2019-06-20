from rest_framework import routers, serializers, viewsets

from Alumno.models import Alumno

from drf_dynamic_fields import DynamicFieldsMixin

class AlumnoSerializers(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('id','profesorAsig','address','name','ap_pat','ap_mat','matricula','materia','telefono','edad','sexo','fechaNacimiento')

