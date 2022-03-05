from django.shortcuts import render
from .models import Post




# Create your views here.
def home(request) :

  context = {
    'posts': Post.objects.all(),
    'title': 'Home',
  }

  return render(request, 'blog/home.html', context)




def messenger(request) :

  context = {
      
      'title': 'Messenger'
    }

  return render(request, 'blog/messenger.html', context)




def add_post(request) :

  context = {
    'title': 'Posts'
  }

  return render(request, 'blog/post.html', context)




def profile(request) :

  context = {
    'title': 'Profile'
  }

  return render(request, 'blog/profile.html', context)
