__author__ = 'heddevanderheide'

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class ModelX(models.Model):
    x = models.CharField(max_length=64)

    def __str__(self):              # __unicode__ on Python 2
        return self.x


@python_2_unicode_compatible
class ModelY(models.Model):
    x = models.ForeignKey(ModelX)
    y = models.CharField(max_length=64)

    def __str__(self):              # __unicode__ on Python 2
        return self.y