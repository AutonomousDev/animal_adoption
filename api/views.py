from django.apps import apps
from .serializers import AnimalSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def animal_list(req):
    animals = apps.get_model("animals", "Animal").objects.all()
    serialized = AnimalSerializer(animals, many=True)
    print(serialized)
    return Response(serialized.data)
