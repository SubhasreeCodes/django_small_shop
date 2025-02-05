
from rest_framework import viewsets, status
from rest_framework.response import Response

from backend.models import Category
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {
            'data': serializer.data
        }
        return Response(data)