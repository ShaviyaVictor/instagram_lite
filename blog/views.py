from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.
def home(request) :

  return HttpResponse('<h1>Blog Home</h1>')



def messenger(request) :

  return HttpResponse('<h1>Blog Messenger</h1>')



def add_post(request) :

  return HttpResponse('<h1>Blog Post</h1>')



def profile(request) :

  return HttpResponse('<h1>Blog Profile</h1>')