from django.db import models

class List(models.Model):
	lan = models.CharField(max_length=20)

class Item(models.Model):
	text = models.TextField()
	lst = models.ForeignKey(List, on_delete=models.CASCADE)
	name = models.CharField(max_length=20, default='')