
from . import views
from django.urls import path
from django.conf.urls import include ,url


urlpatterns = (
    # path('', views.index),
    # path(r'^(d)$', views.show),
    url(r'^$',views.index),
    url(r'^(\d+)$',views.show)
)
