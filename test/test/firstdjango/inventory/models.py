from django.db import models
from mongoengine import *

class item(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	amount = models.IntegerField()
