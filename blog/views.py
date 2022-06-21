from msilib.schema import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy

from blog.models import Post

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "all_posts_list"


class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:all')


class PostDetailView(DetailView):
    model = Post 


class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:all')
    

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:all')