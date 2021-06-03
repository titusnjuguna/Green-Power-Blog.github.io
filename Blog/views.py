from django.shortcuts import render,reverse
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post
# Create your views here.
def home(request):
    context={
        'Posts': Post.objects.all()
            }
    return render(request,'Blog/index.html',context)
    
class PostListView(ListView):
    model = Post
    template_name= 'Blog/index.html'
    context_object_name = 'Posts'

    def get_querySet(self):
        return Post.objects.order_by('-date_created')
class PostDetailView(DetailView):
     model=Post 
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields=['title','summary','content','header_image']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Post
    fields=['title','content','header_image']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post= self.get_object()
        if self.request.user == post.author:
            return True
        return False     
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post= self.get_object()
        if self.request.user == post.authhor:
            return True
        return False


