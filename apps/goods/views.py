
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters,generics
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view

# from rest_framework.pagination import PageNumberPagination
import json



from goods.serializers import GoodsSerializers,BannerSerializers
from goods.models import Goods,Banner
from goods.filters import GoodsFilter
from utils.mixins_base import mListModelMixin,mCreateModelMixin,mRetrieveModelMixin,CustomModelViewSet
from collections import OrderedDict
from utils.pagination_base import  PageNumberPagination
class GoodsPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100



class GoodsListViewSet(mListModelMixin,mCreateModelMixin,viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializers
    pagination_class = GoodsPagination #分页

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'shop_price')


    def retrieve(self, request, *args, **kwargs):
         instance = self.get_object()
         instance.click_num += 1
         instance.save()
         serializer = self.get_serializer(instance)
         headers = self.get_success_headers(serializer.data)
         return Response({
            "msg": "",
            "data": serializer.data,
            "code": 200
         }, status=status.HTTP_201_CREATED, headers=headers)



class BannerViewSet(CustomModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializers