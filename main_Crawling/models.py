#-*- coding:utf-8 -*-

from django.db import models





# Create your models here.
class Crawling(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    sale = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    img_src = models.URLField()

    objects = models.Manager()
