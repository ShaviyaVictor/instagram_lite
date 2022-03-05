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



  return render(request, 'blog/messenger.html', {'title':'Messenger'})




def add_post(request) :

  return render(request, 'blog/post.html')




def profile(request) :

  return render(request, 'blog/profile.html')
