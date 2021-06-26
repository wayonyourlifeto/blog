from django.shortcuts import render
from django.views.generic import ListView, DetailView #new 24/06
from django.views.generic.edit import CreateView, UpdateView #new 26/06
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView): #new
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

# Create your views here.
