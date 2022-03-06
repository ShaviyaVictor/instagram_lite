from django.urls import path
from .views import PostListView, PostDetailView
from . import views



urlpatterns = [

    # path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),

    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    path('messenger/', views.messenger, name='blog-messenger'),
    path('post/', views.add_post, name='blog-post'),
    
]