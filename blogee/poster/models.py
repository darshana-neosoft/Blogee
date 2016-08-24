from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Poster(models.Model):
	article = models.CharField(max_length=255)
	author  = models.CharField(max_length=255)




