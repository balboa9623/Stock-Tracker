"""stock_investment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from stock_investment import views

urlpatterns = [
    # TODO - create a HOME PAGE with little to no functionality
    path('', views.HomePage.as_view(), name='home'),
    path('test/', views.LoginPage.as_view(), name='loginHome'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    # 'django.contrib.auth.urls': Allows us to connect to django's built-in authorisations
    path('accounts/', include('django.contrib.auth.urls')),
    # path('trade_details/', include('trade_details.urls')),

    path('transfers/', include('transfers.urls', namespace='transfers')),

    path('trades/', include('TradeDetails.urls', namespace='trade')),

    path('admin/', admin.site.urls),
]
