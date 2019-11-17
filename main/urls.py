#-*- coding:utf-8 -*-


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from main_Crawling import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main_Crawling/', include('main_Crawling.urls')),
]
