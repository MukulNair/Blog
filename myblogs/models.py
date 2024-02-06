from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Blog_Category(models.Model):
    blog_cat = models.CharField(max_length=60, unique=True)
    blog_img = models.ImageField(upload_to='images/')
    blog_description=models.CharField(max_length=1000)
    def __str__(self):
            return self.blog_cat

class contact_info(models.Model):
      u_email = models.EmailField()
      u_message = models.CharField(max_length=200)
      def __str__(self):
            return self.u_email
      
class SubscribedUser(models.Model):
    #name = models.CharField(max_length=100)
    u_email = models.EmailField(max_length=100, unique=True)
    # created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self):
        return self.u_email
    
class blog_post(models.Model):
    blog_name =models.CharField(max_length=100)
    cover_img=models.ImageField(upload_to='images/')
    like_btn=models.IntegerField(default=0,null=True)
    view_btn=models.IntegerField(default=0,null=True)
    blog_description=RichTextField()
    blog_cat = models.ForeignKey(Blog_Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog_name
    
class Comment(models.Model):
    post = models.ForeignKey(blog_post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.author)