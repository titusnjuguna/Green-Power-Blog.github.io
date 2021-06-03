from django import forms
from .models import Post

class PostCreateForm(forms.Form):
    class Meta:
        model = Post
        fields = ('title','summary','Content','header_image')


#class PostUpdateForm(forms.Form):
    #class Meta:
#model = Post
       # fields = ('title','content','summary','header_image')    