# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BlogArticle(models.Model):
    title = models.CharField(max_length= 50)
    author = models.CharField(max_length= 20)
    time = models.IntegerField(default = 0)