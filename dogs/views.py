from django.shortcuts import render
from .models import Dog, Breed
from .serializers import BreedSerializer, DogSerializer
from rest_framework import viewsets


class DogViewset(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


class BreedViewset(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
