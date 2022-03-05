from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required
def home(request) :

  context = {
    'posts': Post.objects.all(),
    'title': 'Home',
  }

  return render(request, 'blog/home.html', context)



@login_required
def messenger(request) :

  context = {
      
      'title': 'Messenger'
    }

  return render(request, 'blog/messenger.html', context)



@login_required
def add_post(request) :

  context = {
    'title': 'Posts'
  }

  return render(request, 'blog/post.html', context)
