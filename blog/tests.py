from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User


# Create your tests here.
class PostTestClass(TestCase) :

  # Setting up the instance
  def setUp(self) :

    # Creating a new profile
    self.josphine = User(first_name='Josphine', last_name ='Mbaisi', email ='mbaisijosphine@gmail.com')

    self.josphine.save()


  # Testing the posts save functionality
  def test_save_method(self) :

    # Creating a new Post and saving it
    self.new_post = Post(img_title='Test Post', img_caption='This is a random test post', profile=self.josphine)

    self.new_post.save_post()

    all_post = Post.objects.all()

    self.assertTrue(len(all_post) > 0)


  
  # # Testing the posts delete functionality
  # def test_delete_method(self) :

  #   # Creating a new Post and saving it
  #   self.new_post = Post(img_title='Test Post', img_caption='This is a random test post', profile=self.josphine)

  #   self.new_post.delete_post()

  #   all_post = Post.objects.all()

  #   self.assertTrue(len(all_post) -+1)



