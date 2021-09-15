#from django.shortcuts import render no lo necesitamos
from django.core.exceptions import AppRegistryNotReady
from django.http import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers 

# Create your views here.

class HelloApiView(APIView):
    """API View de prueba"""
    serializer_class = serializers.HelloSerializer
    def get(self,request,format=None):
        """retornar lista de caracteristicas de APIView"""
        an_apiview=[
            'Usamos metodos HTTP como funciones (get,post, patch, delete, put,)',
            'Es similar a una vista tradicional de Dajanfo',
            'Nos da el mayor control sobre la logica de nuestra aplicacion',
            'Esta mapeando manualmente a los URLs'
        ]
        return Response({'message': 'Hello', 'an_apiview':an_apiview})

    def post(self,request):
        """crea un mensaje con nuestro nombre"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
    def put(self, request,pk=None):
        """maneja actualizar un objeto"""
        return Response({'method':'PUT'})
    def patch(self, resquest,pk=None):
        """actualizacion parcial de un objeto"""
        return Response({'method':'PATCH'})
    def delete(self, resquest,pk=None):
        """borrar un objeto"""
        return Response({'method':'DELETE'})
