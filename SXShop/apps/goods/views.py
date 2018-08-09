
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework.pagination import PageNumberPagination


from goods.serializers import GoodsSerializers
from goods.models import Goods


class GoodsPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100



# class GoodsListViews(APIView):
#
#     def get(self,request,format = None):
#         goods = Goods.objects.all()[:10]
#         goods_serializer = GoodsSerializers(goods,many=True)
#         return Response(goods_serializer.data)

class GoodsListViews(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializers
    pagination_class = GoodsPagination

    # filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_class = GoodsFilter
    # search_fields = ('name', 'goods_brief', 'goods_desc')
    # ordering_fields = ('sold_num', 'shop_price')
    #
    # def retrieve(self, request, *args, **kwargs):
    #      instance = self.get_object()
    #      instance.click_num += 1
    #      instance.save()
    #      serializer = self.get_serializer(instance)
    #      return Response(serializer.data)