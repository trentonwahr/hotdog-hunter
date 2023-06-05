from django.db import models

class Hotdog(models.Model):
  restaurant = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  description = models.TextField(max_length=300)
  rating = models.IntegerField(choices=list(zip(range(1,6), range(1,6))))
  
  def __str__(self):
    return self.restaurant
  