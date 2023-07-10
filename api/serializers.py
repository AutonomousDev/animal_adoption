from rest_framework.serializers import ModelSerializer
from django.apps import apps


class AnimalSerializer(ModelSerializer):
    class Meta:
        model = apps.get_model("animals", "Animal")
        fields = "__all__"
