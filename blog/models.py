from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone






# Create your models here.
class Post(models.Model) :
  img_title = models.CharField(max_length=100)
  img_caption = models.CharField(max_length=500)
  profile = models.ForeignKey(User, on_delete=models.CASCADE)
  date_posted = models.DateTimeField(default=timezone.now)



  def __str__(self) -> str:
      return self.date_posted

  class Meta :
    ordering = ['-date_posted']