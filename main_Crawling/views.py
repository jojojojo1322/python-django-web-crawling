# api/views.py
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status

from .serializers import CrawlingSerializer
from .models import Crawling

from rest_framework.response import Response



class CrawlingView(viewsets.ModelViewSet):
    queryset = Crawling.objects.all()
    serializer_class = CrawlingSerializer

