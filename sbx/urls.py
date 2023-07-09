"""
URL configuration for sbx project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from sbx.views import home
from .views import get_dynamic_value
from sbx.views import signup
from sbx.views import Login
from sbx.views import platform
from sbx.views import data_endpoint,get_Dynamiccoin,transaction_table_view,logout_view,dataset_view,add_cash
from sbx.views import price
from sbx.views import usern
from sbx.views import platform_coin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Login,name='login'),
    path('signup/',signup,name='signup'),
    path('home/',home,name='home'),
    path('home/platform/',platform,name='platform'),
    path('get_dynamic_value/', get_dynamic_value, name='get_dynamic_value'),
    path('data_endpoint/', data_endpoint, name='data_endpoint'),
    path('price/', price, name='price'),
    path('usern/',usern,name='usern'),
    path('platform_coin/',platform_coin,name='platform_coin'),
    path('add_cash/',add_cash,name='add_cash'),
    path('get_Dynamiccoin/', get_Dynamiccoin, name='get_Dynamiccoin'),
    path('transaction_table_view/', transaction_table_view, name='transaction_table_view'),
    path('logout/', logout_view, name='logout'),
    path('dataset_view/', dataset_view, name='dataset_view'),
    
]
