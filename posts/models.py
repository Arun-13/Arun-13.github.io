# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from datetime import datetime

# Create your models here.

class Posts(models.Model):
     Name = models.CharField(max_length=35)
     Title = models.CharField(max_length=200)
     Content =models.TextField()
     Image = models.ImageField(upload_to='post_image',blank=True)
     Created_At = models.DateTimeField(default=datetime.now,blank=True)
     def __str__(self):
          return self.Name + "" + self.Title 
     class Meta:
          verbose_name_plural="Posts"
