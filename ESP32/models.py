from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class ESP32(models.Model):
    id_user =   models.ForeignKey(User, on_delete = models.SET(-1))
    num_esp32 = models.IntegerField(null=False)
    mac_esp32 =  models.CharField(max_length=100, null=False)
    delete = models.BooleanField (default = True)
    date_now = models.DateTimeField(default = timezone.now)
 

    def __str__(self):
        return self.id


    class Meta:
        db_table = 'ESP32'