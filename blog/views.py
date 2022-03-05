from django.shortcuts import render



# Create your views here.
def home(request) :

  return render(request, 'blog/home.html')



def messenger(request) :

  return render(request, 'blog/messenger.html')




def add_post(request) :

  return render(request, 'blog/post.html')




def profile(request) :

  return render(request, 'blog/profile.html')
