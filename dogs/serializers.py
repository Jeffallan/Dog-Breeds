from rest_framework.serializers import ModelSerializer
from .models import Dog, Breed

class DogSerializer(ModelSerializer):
    class Meta:
        model = Dog
        fields = "__all__"
        #depth = 2

class BreedSerializer(ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"