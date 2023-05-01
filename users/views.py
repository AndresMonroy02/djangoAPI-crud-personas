from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Personas
from .serializer import PersonesSerializer
from rest_framework import generics

# personas by id - get, update, delete
class PersonaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personas.objects.all()
    serializer_class = PersonesSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'HEAD', 'OPTIONS', 'TRACE']


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# get personas
class PersonasList(generics.ListCreateAPIView):
    queryset = Personas.objects.all()
    serializer_class = PersonesSerializer

def helloWorld(HttpRequest):
    return HttpResponse("Hello World!")