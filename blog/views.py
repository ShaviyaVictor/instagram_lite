from django.shortcuts import render




# Dummy data to pass it as variable

posts = [
  {

    'author': 'Victor Shaviya',
    'title': 'Adventure',
    'caption': 'Huh! You must have enjoyed',
    'date_posted': 'Aug 10, 1996'

  },
  {

    'author': 'Josphine Mbaisi',
    'title': 'Voyage',
    'caption': 'The journey was indeed very long',
    'date_posted': 'March 10, 2018'

  },
]

# Create your views here.
def home(request) :

  context = {
    'posts': posts,
    'title': 'Home'
  }

  return render(request, 'blog/home.html', context)




def messenger(request) :

  context = {
      'posts': posts,
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
