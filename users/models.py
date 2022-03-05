from django.db import models

# Create your models here.
class NewsLetterRecipients(models.Model):
    username = models.CharField(max_length = 30)
    email = models.EmailField()
