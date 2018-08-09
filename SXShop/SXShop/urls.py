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
# from django.urls import path
from django.conf.urls import url,include
from SXShop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

# import xadmin


from goods.views import GoodsListViews

router = DefaultRouter()

#配置goods的url
router.register(r'goods', GoodsListViews, base_name="goods")
#
#
#
#
#
# goods_list = GoodsListViews.as_view({
#     'get': 'list',
# })

urlpatterns = [
    url('admin/', admin.site.urls),
    # url(r'xadmin/', include(xadmin.site.urls)),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    # url(r'goods/$', GoodsListViews.as_view(),name="goods_list"),

    url(r'docs/',include_docs_urls(title='b'))

]
