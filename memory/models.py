from django.db import models
from django.contrib.auth import get_user_model

class Story(models.Model):
  title = models.CharField(max_length=255)
  body = models.TextField(default="")
  author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

  def __str__(self):
    return self.title
