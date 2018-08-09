# -*- coding: utf-8 -*-
#  SXShop  ---  2018/4/22  ---  PyCharm
__author__ = 'lishunfeng'


from django.views.generic.base import View
from django.views.generic import ListView
from goods.models import Goods
from django.forms.models import model_to_dict


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