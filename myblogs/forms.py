from.models import Blog_Category,blog_post,Comment
from django.forms import ModelForm
 


class Blog_Form(ModelForm):
    class Meta:
         model = Blog_Category
         fields = "__all__"


class BlogPost_Form(ModelForm):
    class Meta:
         model = blog_post
         exclude=["like_btn","view_btn"]

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
