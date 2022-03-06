from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .email import send_welcome_email
from .models import NewsLetterRecipients



# Create your views here.

def register(request) :

  if request.method == 'POST' :

    form = UserRegisterForm(request.POST)
    if form.is_valid() :
      form.save()

      username = form.cleaned_data.get('username')

      email = form.cleaned_data.get('email')

      recipient = NewsLetterRecipients(username=username, email=email)
      recipient.save()
      send_welcome_email(username, email)


      messages.success(request, f'Account successfully created for {username}! Login to continue.')

      return redirect('login')

  else :
    form = UserRegisterForm()


  return render(request, 'users/register.html', {'form': form})



@login_required
def profile(request) :

  u_form = UserUpdateForm()
  p_form = ProfileUpdateForm()

  context = {
    'title': 'Profile',
    'u_form': u_form,
    'p_form': p_form

  }

  return render(request, 'users/profile.html', context)



