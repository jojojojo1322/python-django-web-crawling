# api/urls.py
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from .views import CrawlingView



crawling_list = CrawlingView.as_view({
    'get': 'list',
})
crawling_detail = CrawlingView.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
})


urlpatterns = format_suffix_patterns([
    
    path('', crawling_list, name='crawling_list'),
    path('<int:pk>/', crawling_detail, name='crawling-detail'),

    
])
