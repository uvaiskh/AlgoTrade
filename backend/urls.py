from django.urls import path

from . import views
from common.constants import UrlNames


urlpatterns = [
    path('test', views.TestView.as_view(), name=UrlNames.Test),
    path('tokens', views.TokenView.as_view(), name=UrlNames.Tokens),
    path('orders', views.PlaceOrderSerializer.as_view(), name=UrlNames.Orders)
]