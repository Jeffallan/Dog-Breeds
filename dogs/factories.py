"""
adapted from https://mattsegal.dev/django-factoryboy-dummy-data.html
to generate test data
"""

import factory # type: ignore
from factory.django import DjangoModelFactory # type: ignore
import random

from .models import Breed, Dog

class BreedFactory(DjangoModelFactory):
    class Meta:
        model = Breed
    name = factory.Faker("last_name")
    size = factory.Faker("random_choices", elements=[Breed.TINY, Breed.SMALL, Breed.MEDIUM, Breed.LARGE], length=1)
    friendliness = factory.Faker("random_int", min=1, max=5)
    trainability = factory.Faker("random_int", min=1, max=5)
    sheddingamount = factory.Faker("random_int", min=1, max=5)
    exerciseneeds = factory.Faker("random_int", min=1, max=5)


class DogFactory(DjangoModelFactory):
    class Meta:
        model = Dog
    name = factory.Faker("first_name")
    age = factory.Faker("random_int", min=0, max=25)
    gender = factory.Faker("random_choices", elements=[Dog.FEMALE, Dog.MALE])
    breed = factory.SubFactory(BreedFactory)
    color = factory.Faker("random_choices", elements=["Black", "Blue", "Yellow", "White"], length=1)
    favoritefood = factory.Faker("random_choices", elements=["wet", "dry", "all the treats"], length=1)
    favoritetoy = factory.Faker("random_choices", elements=["puzzle feeder", "squeeky", "cats"], length=1)