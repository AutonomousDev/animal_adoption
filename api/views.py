from django.apps import apps
from .serializers import AnimalSerializer, NewsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination

class AnimalFilterView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = apps.get_model("animals", "Animal").objects.all()
        serializer = AnimalSerializer(queryset, many=True)

        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data
        queryset = apps.get_model("animals", "Animal").objects.filter(**data)
        serializer = AnimalSerializer(queryset, many=True)
        
        return Response(serializer.data, status=200)

class NewsListView(ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = apps.get_model("news", "News").objects.all()
    serializer_class = NewsSerializer
    pagination_class = LimitOffsetPagination

    # Examples:
    # 127.0.0.1:8000/api/news/
    # 127.0.0.1:8000/api/news/?limit=1&offset=6
    # 127.0.0.1:8000/api/news/?limit=3