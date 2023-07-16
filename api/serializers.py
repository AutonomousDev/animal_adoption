from rest_framework.serializers import ModelSerializer
from django.apps import apps

class AnimalSerializer(ModelSerializer):
    class Meta:
        model = apps.get_model("animals", "Animal")
        # writing out field names here for easier reference
        fields = [
            "date_entered",
            "name",
            "species",
            "age",
            "breed",
            "shelter",
            "views",
            "availability",
            "disposition",
            "size",
        ]

class SpeciesSerializer(ModelSerializer):
    class Meta:
        model = apps.get_model("animals", "Species")
        fields = ["name"]

class BreedSerializer(ModelSerializer):
    class Meta:
        model = apps.get_model("animals", "Breed")
        fields = ["name"]

class SizeSerializer(ModelSerializer):
    class Meta:
        model = apps.get_model("animals", "Size")
        fields = ["name"]

class AvailabilitySerializer(ModelSerializer):
    class Meta:
        model = apps.get_model("animals", "Availability")
        fields = ["availability"]

class DispositionSerializer(ModelSerializer):
    class Meta:
        model = apps.get_model("animals", "Disposition")
        fields = ["disposition"]

class NewsSerializer(ModelSerializer):
    class Meta:
        model = apps.get_model("news", "News")
        fields = [
            "title",
            "body",
            "date_created",
            "author",
            "animal",
        ]

class ShelterSerializer(ModelSerializer):
    class Meta:
        model = apps.get_model("shelters", "Shelter")
        fields = [
            "name",
            "addressLine1",
            "addressLine2",
            "addressLine3",
            "city",
            "state",
            "zip",
            "phoneNumber",
            "webSite"
        ]
