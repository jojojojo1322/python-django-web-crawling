# api/serializers.py
from rest_framework import serializers
from .models import Crawling



class CrawlingSerializer(serializers.HyperlinkedModelSerializer):
    # comments = serializers.StringRelatedField(many=True)

    class Meta:
        model = Crawling
        fields = (
            'url',
            'id',
            'area',
            'title',
            'sale',
            'price',
            # 'comments',
        )
