from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView





# Create your views here.
@login_required
def home(request) :

  context = {
    'posts': Post.objects.all(),
    'title': 'Home',
  }

  return render(request, 'blog/home.html', context)



class PostListView(ListView) :

  model = Post

  template_name = 'blog/home.html'
  context_object_name = 'posts'



class PostDetailView(DetailView) :

  model = Post



class PostCreateView(CreateView) :

  model = Post





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
