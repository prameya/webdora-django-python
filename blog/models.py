# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BlogPosts(models.Model):
    title = models.CharField(max_length = 100)
    timestamp = models.DateTimeField()
    bodytext = models.TextField()
    tags = models.CharField(maxlength=200)

    class Admin:
       pass