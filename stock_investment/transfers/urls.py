from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'transfers'

urlpatterns = [
    path('by/(?<username>[-\w]+)/', views.UserTransferList.as_view(), name='user_all'),
    # path('new/', views.TransferCreateView.as_view(), name='transfer_new'),
    # # 'username' & 'pk' is returned from get_absolute_url() function defined in models.py.
    # # the path finds details of a single transaction, based on the username and pk provided.
    # path('usr/(?P<username>[-\W]+)/(?P<pk>\d+)/', views.TransferDetailsView.as_view(), name='single'),
]