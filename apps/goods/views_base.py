# -*- coding: utf-8 -*-
#  SXShop  ---  2018/4/22  ---  PyCharm
__author__ = 'lishunfeng'


from django.views.generic.base import View
from django.views.generic import ListView
from .models import Goods
from django.forms.models import model_to_dict
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class GoodsListView(View):
    def get(self, requset):

        json_list = []
        goods = Goods.objects.all()

        for good in goods:
            json_dict = model_to_dict(good)
            json_list.append(json_dict)

        from django.http import HttpResponse ,JsonResponse
        from django.core import serializers
        json_data = serializers.serialize('json',goods)
        import json

        # return HttpResponse(json_data,content_type="application/json")
        return JsonResponse(json.loads(json_data),safe=False)

class ListView(object):
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        re_dict = {}
        re_dict["data"] = serializer.data
        re_dict["code"] = 0
        re_dict["msg"] = ""

        return Response(re_dict)