from django.db import models

# Create your models here.

class Books(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  rating = models.IntegerField(default = 1)
  notes = models.TextField(blank = True)
  date_added = models.DateTimeField(auto_now_add = True)

  def __str__(self):
    return self.title

  
  def rating_stars(self):
    return "⭐" * self.rating