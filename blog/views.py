from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin





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



class PostCreateView(LoginRequiredMixin, CreateView) :

  model = Post

  fields = [
    'img_title',
    'img_caption',
    'image'
  ]

  def form_valid(self, form) :
    form.instance.profile = self.request.user
    return super().form_valid(form)





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
