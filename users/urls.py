from django.urls import path
from django import urls
from .views import PersonaDetail, PersonasList, helloWorld

urlpatterns = [
    path('personas/', PersonasList.as_view(), name='Personas'),
    path('personas/<int:pk>', PersonaDetail.as_view(), name='Personas'),
    path('hello/', helloWorld, name='Hello'),
]