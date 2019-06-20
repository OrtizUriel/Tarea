from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serializers, viewsets

from Administrador import views

urlpatterns = [
    re_path(r'^lista/$', views.AdministradorList.as_view()),
    re_path(r'^detailAdmin/(?P<pk>\d+)/$', views.AdministradorList.as_view()),
    re_path(r'^detalle/(?P<pk>\d+)$', views.AdministradorDetail.as_view()),

]
