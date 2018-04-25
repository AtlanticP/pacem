from django.db import models

class List(models.Model):
	pass

class Item(models.Model):
	text = models.CharField(max_length=50)
	lst = models.ForeignKey(List, on_delete=models.CASCADE)