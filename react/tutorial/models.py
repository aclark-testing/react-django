from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Comment(models.Model):
    comment = models.CharField(max_length=300, blank=True, null=True)
    name = models.CharField(max_length=300, blank=True, null=True)
