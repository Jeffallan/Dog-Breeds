from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Breed(models.Model):

    TINY = "Tiny"
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"

    SIZE_CHOICES = [(TINY, "Tiny"), (SMALL, "Small"), (MEDIUM, "Meduim"), (LARGE, "Large")]

    name = models.CharField(max_length=50)
    size = models.CharField(choices=SIZE_CHOICES, default=MEDIUM, max_length=6)
    friendliness = models.PositiveIntegerField(default=1,
                                               validators=[MaxValueValidator(5), MinValueValidator(1)])
    trainability = models.PositiveIntegerField(default=1,
                                               validators=[MaxValueValidator(5), MinValueValidator(1)])
    sheddingamount = models.PositiveIntegerField(default=1,
                                               validators=[MaxValueValidator(5), MinValueValidator(1)])
    exerciseneeds = models.PositiveIntegerField(default=1,
                                               validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __stf__(self) -> str:
        return self.name

class Dog(models.Model):

    FEMALE = 'F'
    MALE = 'M'

    GENDER_CHOICES = [(FEMALE, "Female"), (MALE, "Male")]

    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(25)])
    breed = models.ForeignKey(Breed, on_delete=models.DO_NOTHING)
    gender = models.CharField(choices=GENDER_CHOICES, default=FEMALE, max_length=6)
    color = models.CharField(max_length=60, blank=True)
    favoritefood = models.CharField(max_length=60, blank=True)
    favoritetoy = models.CharField(max_length=60, blank=True)

    def __str__(self) -> str:
        return self.name
