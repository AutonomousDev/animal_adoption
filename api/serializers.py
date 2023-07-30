from rest_framework.serializers import ModelSerializer
from django.apps import apps
from django.contrib.auth.models import User

class SpeciesSerializer(ModelSerializer):
    class Meta:
        model = apps.get_model("animals", "Species")
        fields = ["id", "name"]
        read_only_fields = ["id", "name"]

class BreedSerializer(ModelSerializer):
    class Meta:
        model = apps.get_model("animals", "Breed")
        fields = ["id", "name"]
        read_only_fields = ["id", "name"]

class SizeSerializer(ModelSerializer):
    class Meta:
        model = apps.get_model("animals", "Size")
        fields = ["id", "name"]
        read_only_fields = ["id", "name"]

class AvailabilitySerializer(ModelSerializer):
    class Meta:
        model = apps.get_model("animals", "Availability")
        fields = ["id", "availability"]
        read_only_fields = ["id", "availability"]

class DispositionSerializer(ModelSerializer):
    class Meta:
        model = apps.get_model("animals", "Disposition")
        fields = ["id", "disposition"]
        read_only_fields = ["id", "disposition"]

class ShelterSerializer(ModelSerializer):
    class Meta:
        model = apps.get_model("shelters", "Shelter")
        fields = [
            "id",
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
        read_only_fields = ["id"]

class UserSerializer(ModelSerializer):
    # Using the example:
    # https://www.django-rest-framework.org/api-guide/serializers/#additional-keyword-arguments
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
            username=validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()

        return user
    
class AnimalSerializer(ModelSerializer):
    species = SpeciesSerializer()
    breed = BreedSerializer()
    shelter = ShelterSerializer()
    availability = AvailabilitySerializer()
    size = SizeSerializer()
    disposition = DispositionSerializer()

    class Meta:
        model = apps.get_model("animals", "Animal")
        # writing out field names here for easier reference
        fields = [
            "id",
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
            "image",
        ]
        read_only_fields = ["id", "shelter", "views", "date_entered"]

class NewsSerializer(ModelSerializer):
    author = UserSerializer(read_only=True)
    animal = AnimalSerializer()

    class Meta:
        model = apps.get_model("news", "News")
        fields = [
            "id",
            "title",
            "body",
            "date_created",
            "author",
            "animal",
        ]
        read_only_fields = ["id", "author", "date_created"]