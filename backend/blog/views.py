from django.shortcuts import render
from .models import Posts
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView

class PostListView(ListView):
    pass

class PostDetailView(DetailView):
    pass

class PostCreateView(CreateView):
    pass

class PostUpdateView(UpdateView):
    pass

class PostDeleteView(DeleteView):
    pass
