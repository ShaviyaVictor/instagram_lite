from django.urls import path
from . import views



urlpatterns = [

    path('', views.home, name='blog-home'),
    path('messenger/', views.messenger, name='blog-messenger'),
    path('post/', views.add_post, name='blog-post'),
    
]