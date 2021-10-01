from django.core.management.base import BaseCommand
from django.db import models, transaction

from dogs.models import Dog, Breed
from dogs.factories import BreedFactory, DogFactory

BREEDS = 10
DOGS = 25

class Command(BaseCommand):
    help = "generates test data for the dog application"

    models = [Dog, Breed]

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("removing old data")
        Dog.objects.all().delete()
        Breed.objects.all().delete()
        self.stdout.write("creating new data")
        #breeds = []
        for _ in range(BREEDS):
            breed = BreedFactory()
            #breed.append
        for _ in range(DOGS):
            dog = DogFactory()
