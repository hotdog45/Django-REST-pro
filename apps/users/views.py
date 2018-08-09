from django.shortcuts import render

# Create your views here.
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from random import choice
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework.decorators import action

from rest_framework import authentication
from rest_framework import permissions


from utils.yunpian import YunPian
from SXShop.settings import APIKEY
from users.models import VerifyCode
from users.serializers import smsSerializers, UserRegSerializer, UserDetailSerializer
from utils.mixins_base import mListModelMixin,mCreateModelMixin,mRetrieveModelMixin,CustomModelViewSet,mUpdateModelMixin



User = get_user_model()



class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

class SmsSendCodeViewset(viewsets.GenericViewSet):
    #发送验证码

    serializer_class = smsSerializers

    def generate_code(self):
        #生成四位数字的验证码

        seeds = "0123456789"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data["mobile"]

        yun_pian = YunPian(APIKEY)
        code = self.generate_code()

        sms_dic = yun_pian.send_sms(code=code,mobile=mobile)
        print(sms_dic)

        if sms_dic["code"] != 0 :
            return Response({
                "msg":sms_dic["msg"],
                "data":{
                    "mobile": mobile
                },
                "code":400
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code,mobile=mobile)
            code_record.save()
            return Response({
                "msg": "验证码发送成功",
                "data": {
                    "mobile": mobile
                },
                "code": 200
            }, status=status.HTTP_200_OK)

class UserViewset(mCreateModelMixin, mUpdateModelMixin, mRetrieveModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication,authentication.SessionAuthentication)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        elif self.action == "create":
            return UserRegSerializer
        return UserDetailSerializer
    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        else:
            return []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response({
            "msg":"注册成功",
            "data":re_dict,
            "code":200
        }, status=status.HTTP_201_CREATED, headers=headers)

    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()

    # @action(methods=['get'], detail=True)
    # def balance(self, request, pk=None):
    #     user = self.get_object()
    #     # user_treasure = user.record_set.values('coin_type').annotate(Sum('amount'))
    #     return Response(user_treasure)