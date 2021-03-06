from django.urls import path
from django.urls.conf import include
from rest_framework import viewsets
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("dogs", views.DogViewset)
router.register("breeds", views.BreedViewset)

urlpatterns = [
    path("", include(router.urls))
]