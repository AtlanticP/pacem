from django.db import models

class List(models.Model):
  
  lan = models.CharField(max_length=20)
  
  def __str__(self):
    return self.lan


class Item(models.Model):
  
  lst = models.ForeignKey(List, on_delete=models.CASCADE, default='')
  code = models.TextField()
  name = models.CharField(max_length=20, default='')
  name_r = models.CharField(max_length=20, default='') # to use for russian language
  description = models.CharField(max_length=500, default='')
  description_r = models.CharField(max_length=500, default='') # to use for russian language

  def __str__(self):
    return self.name

class Graph(models.Model):
  
  termin = models.CharField(max_length=20, default='')
  definition = models.TextField()
  # description = models.TextField()
  lst = models.ForeignKey(List, on_delete=models.CASCADE)

