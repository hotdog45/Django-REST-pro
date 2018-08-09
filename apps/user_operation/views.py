from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from user_operation.serializers import  AddressSerializer
from user_operation.models import  UserAddress
from utils.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response


class AddressViewset(viewsets.ModelViewSet):
    """
    收货地址管理
    list:
        获取收货地址
    create:
        添加收货地址
    update:
        更新收货地址
    delete:
        删除收货地址
    """
    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    # authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    # serializer_class = AddressSerializer

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)

    # @action(methods=['get'], detail=True)
    # def balance(self, request, pk=None):
    #     user = self.get_object()
    #     user_treasure = user.record_set.values('coin_type').annotate(Sum('amount'))
    #     return Response(user_treasure)