from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'transfers'

urlpatterns = [
    path('usr/(?P<username>[-\w]+)/', views.AllTransactionList.as_view(), name='user_all'),
    path('new/', views.CreateNewTransfer.as_view(), name='new_transfer'),
    # 'username' & 'pk' is returned from get_absolute_url() function defined in models.py.
    # the path finds details of a single transaction, based on the username and pk provided.
    path('usr/(?P<username>[-\W]+)/(?P<pk>\d+)/', views.TransferDetails.as_view(), name='single'),
]