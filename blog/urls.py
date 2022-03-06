from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from . import views



urlpatterns = [

    # path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),

    # template name is post_detail.html
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # template name is post_form.html
    path('post/new/', PostCreateView.as_view(), name='post-create'),

    path('messenger/', views.messenger, name='blog-messenger'),
    path('post/', views.add_post, name='blog-post'),
    
]