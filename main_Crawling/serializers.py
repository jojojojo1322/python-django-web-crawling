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
            'img_src',
            'detail_guide',
            'detail_src',
            # 'comments',
        )