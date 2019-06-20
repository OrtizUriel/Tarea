from django.db import models
from django.contrib.postgres.fields import JSONField
from django.conf import settings
from django.utils import timezone

class Profesor(models.Model):
    address = models.CharField(max_length=250, null= False)
    name =   models.CharField(max_length=100, null=False)
    ap_pat = models.CharField(max_length=100, null=False)
    ap_mat = models.CharField(max_length=100, null=False)
    telefono = models.IntegerField(null=False) 
    edad = models.IntegerField(null=False)
    sexo = models.CharField(max_length=50, null=False)
    yearsExperience = models.IntegerField(null=False)
    fechaNacimiento= models.CharField(max_length=100, null=False)
    created = models.DateTimeField(default = timezone.now)


    def __str__(self):
        return self.name


    class Meta:
        db_table = 'Profesor'
