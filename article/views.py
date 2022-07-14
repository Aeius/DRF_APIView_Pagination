# article/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Article as ArticleModel
from .serializers import ArticleSerializer

# 페이지네이션 관련 class import
from .pagination import PaginationHandlerMixin, BasePagination

# pagination이 필요한 APIView 클래스들에게 PaginationHandlerMixin을 인자로 주면된다
class PaginationTest(APIView, PaginationHandlerMixin):
    pagination_class = BasePagination # query_param 설정 /?page_size=<int>
    serializer_class = ArticleSerializer
    
    def get(self, request):
        instance = ArticleModel.objects.all()
        page = self.paginate_queryset(instance) # page_size, page에 따른 pagination 처리된 결과값
        # 페이징 처리가 된 결과가 반환되었을 경우
        if page is not None:
            # 페이징 처리된 결과를 serializer에 담아서 결과 값 가공
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        # 페이징 처리 필요 없는 경우
        else:
            serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)