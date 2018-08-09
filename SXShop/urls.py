"""SXShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import xadmin

# from django.urls import path
from django.conf.urls import url,include
from SXShop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token


from goods.views import GoodsListViewSet,BannerViewSet
from user_operation.views import AddressViewset
from users.views import SmsSendCodeViewset,UserViewset
router = DefaultRouter()

#配置goods的url
router.register(r'goods', GoodsListViewSet, base_name="goods")
router.register(r'banner', BannerViewSet, base_name="banner")
router.register(r'address', AddressViewset, base_name="address")
router.register(r'code', SmsSendCodeViewset, base_name="code")
router.register(r'user', UserViewset, base_name="user")




urlpatterns = [
    # url('admin/', admin.site.urls),
    url(r'xadmin/', include(xadmin.site.urls)),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),

    url(r'docs/',include_docs_urls(title='b')),
    #drf自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),
    #jwt认证
    url(r'^login/', obtain_jwt_token),
]
