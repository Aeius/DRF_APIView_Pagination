# user/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status

from .models import Article as ArticleModel
from .serializers import ArticleSerializer

from .pagination import PaginationHandlerMixin
from rest_framework.pagination import PageNumberPagination

from rest_framework.pagination import LimitOffsetPagination

class ArticlePagination(PageNumberPagination):
    page_size_query_param = 'limit'
    
class PaginationTest(APIView, PaginationHandlerMixin):
    pagination_class = ArticlePagination
    serializer_class = ArticleSerializer
    
    def get(self, request):
        instance = ArticleModel.objects.all()
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PaginationTest2(APIView, LimitOffsetPagination):
    def get(self, request):
        query = ArticleModel.objects.all()
        results = self.paginate_queryset(query, request, view=self)
        serializers = ArticleSerializer(results, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)