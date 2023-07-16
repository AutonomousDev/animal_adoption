from django.apps import apps
from .serializers import AnimalSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class AnimalFilterView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = apps.get_model("animals", "Animal").objects.all()
        serializer = AnimalSerializer(queryset, many=True)

        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data
        queryset = apps.get_model("animals", "Animal").objects.filter(**data)
        serializer = AnimalSerializer(queryset, many=True)
        
        return Response(serializer.data, status=200)