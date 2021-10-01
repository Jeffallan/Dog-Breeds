"""
adapted from https://mattsegal.dev/django-factoryboy-dummy-data.html
to generate test data
"""

import factory # type: ignore
from factory.django import DjangoModelFactory # type: ignore
import random

from .models import Breed, Dog

def breed_size() -> str:
    return random.choice([Breed.TINY, Breed.SMALL, Breed.MEDIUM, Breed.LARGE])

def dog_color() -> str:
    return random.choice(["Black", "Blue", "Yellow", "White"])

def dog_toy() -> str:
    return random.choice(["puzzle feeder", "squeeky", "cats"])

def dog_food() -> str:
    return random.choice(["wet", "dry", "all the treats"])

def dog_gender() -> str:
    return random.choice([Dog.FEMALE, Dog.MALE])

class BreedFactory(DjangoModelFactory):
    class Meta:
        model = Breed
    name = factory.Faker("last_name")
    size = factory.LazyFunction(breed_size)#.Iterator(Breed.SIZE_CHOICES, getter=lambda x: x[0])#factory.Iterator([Breed.TINY, Breed.SMALL, Breed.MEDIUM, Breed.LARGE], getter=lambda x: x[randint(0,3)])
    friendliness = factory.Faker("random_int", min=1, max=5)
    trainability = factory.Faker("random_int", min=1, max=5)
    sheddingamount = factory.Faker("random_int", min=1, max=5)
    exerciseneeds = factory.Faker("random_int", min=1, max=5)


class DogFactory(DjangoModelFactory):
    class Meta:
        model = Dog
    name = factory.Faker("first_name")
    age = factory.Faker("random_int", min=0, max=25)
    gender = factory.LazyFunction(dog_gender)
    breed = factory.SubFactory(BreedFactory)
    color = factory.LazyFunction(dog_color)
    favoritefood = factory.LazyFunction(dog_food)
    favoritetoy = factory.LazyFunction(dog_toy)