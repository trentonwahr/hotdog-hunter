from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Hotdog(models.Model):
  restaurant = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  description = models.TextField(max_length=300)
  rating = models.IntegerField(choices=list(zip(range(1,6), range(1,6))), default=5)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.restaurant
  
  def get_absolute_url(self):
    return reverse("hotdog-detail", kwargs={"pk": self.id})
  
class Photo(models.Model):
  url = models.CharField(max_length=250)
  hotdog = models.OneToOneField(Hotdog, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for hotdog_id: {self.hotdog_id} @{self.url}"