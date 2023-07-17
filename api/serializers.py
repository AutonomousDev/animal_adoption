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
        read_only_fields = ["shelter", "views", "date_entered"]

class SpeciesSerializer(ModelSerializer):
    class Meta:
        model = apps.get_model("animals", "Species")
        fields = ["name"]
        read_only_fields = ["name"]

class BreedSerializer(ModelSerializer):
    class Meta:
        model = apps.get_model("animals", "Breed")
        fields = ["name"]
        read_only_fields = ["name"]

class SizeSerializer(ModelSerializer):
    class Meta:
        model = apps.get_model("animals", "Size")
        fields = ["name"]
        read_only_fields = ["name"]

class AvailabilitySerializer(ModelSerializer):
    class Meta:
        model = apps.get_model("animals", "Availability")
        fields = ["availability"]
        read_only_fields = ["availability"]

class DispositionSerializer(ModelSerializer):
    class Meta:
        model = apps.get_model("animals", "Disposition")
        fields = ["disposition"]
        read_only_fields = ["disposition"]

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
        read_only_fields = ["author", "date_created"]

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
