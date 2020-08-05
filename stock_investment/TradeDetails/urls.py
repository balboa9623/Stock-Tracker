from django.urls import path, include
from . import views

app_name = 'TradeDetail'

urlpatterns = [
    path('new/', views.AddTradeDetails.as_view(), name='new'),
    path('trade/(?P<username>[-\W]+)/(?P<pk>\d+)/', views.SingleTradeDetails.as_view(), name='single'),
]