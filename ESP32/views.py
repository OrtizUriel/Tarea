# ------------Librerias------------
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# ----------------Modelos--------------
# Nombre app                      nombre modelo
from ESP32.models import ESP32
# ----------------serializers-------------
from ESP32.serializers import ESP32Serializers

# ------------------LIBRERIAS EXTERNAS------------------
# import json

class EspList(APIView):
    # METODO PARA EXPLICITAR LA INFORMACION
    def get(self, request, format=None):
        queryset = ESP32.objects.filter(delete=False)
        #                               ,context = {'request':request}
        serializer = ESP32Serializers(queryset, many=True, context = {'request':request})
        return Response(serializer.data)
    # METODO PARA CREAR NUEVO REGISTRO 
    def post(self, request, format=None):
        serializer = ESP32Serializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response (datas)
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
class EspDetail(APIView):
    #METODO PARA COSULTAR ID Y E RETORNE SI EXISTE O NO
    def get_object(self,pk):
        try: 
            return ESP32.objects.get(pk=pk)
        except ESP32.DoesNotExist:
            raise Http404
    #METODO PARA CONSULTAR ID Y DEVOLVER LOS VALORES DE SUS CAMPOS 
    def get(self, request,pk, format=None):
        esp = self.get_object(pk) 
        serializer = ESP32Serializers(esp)
        return Response(serializer.data)
    #METODO CONSULTAR ID Y ACTUALIZAR DATOS 
    def put(self, request,pk, format=None):
        esp = self.get_object(pk)
        serializer = ESP32Serializers(esp, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        esp = self.get_object(pk)
        serializer = ESP32Serializers(esp, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

