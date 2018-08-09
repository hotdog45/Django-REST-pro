# -*- coding: utf-8 -*-
#  SXShop  ---  2018/5/17  ---  PyCharm
__author__ = 'lishunfeng'
from rest_framework import serializers
from user_operation.models import  UserAddress


class AddressSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(
    #     default=serializers.CurrentUserDefault()
    # )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserAddress
        fields = ("id",  "province", "city", "district", "address", "signer_name", "add_time", "signer_mobile")

