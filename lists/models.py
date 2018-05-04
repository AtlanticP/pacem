from django.db import models

class List(models.Model):
	lan = models.CharField(max_length=20)

class Item(models.Model):
	lst = models.ForeignKey(List, on_delete=models.CASCADE)
	text = models.TextField()
	name = models.CharField(max_length=20, default='')
	description = models.CharField(max_length=50, default='')