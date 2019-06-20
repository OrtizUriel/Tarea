from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serializers, viewsets
# importa todas las vistas exclusivas de la aplicacion 
from . import views 

urlpatterns = [
    re_path(r'^$', views.ProfesorList.as_view()),
    re_path(r'^(?P<pk>\d+)$', views.ProfesorDetail.as_view()),

]
