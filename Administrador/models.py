from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Administrador(models.Model):
    name =   models.CharField(max_length=100, null=False)
    ap_pat = models.CharField(max_length=100, null=False)
    ap_mat = models.CharField(max_length=100, null=False)
    year = models.IntegerField(null=False)
    delete = models.BooleanField (default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name


    class Meta:
        db_table = 'Administrador'
