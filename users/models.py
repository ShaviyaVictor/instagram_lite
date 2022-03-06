from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NewsLetterRecipients(models.Model):
    username = models.CharField(max_length = 30)
    email = models.EmailField()



class Profile(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150)
    profile_img = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self) :
        return f'{self.user.username} Profile'