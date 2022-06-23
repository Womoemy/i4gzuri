from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class Post(models.Model):
  author = models.ForeignKey(get_user_model())
  title = models.CharField(max_length=200)
  text = models.TextField
  created_date = models.DateTimeField
  published_date = models.DateTimeField

  # def __str__(self):
  #   return 