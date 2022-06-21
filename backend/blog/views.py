from django.shortcuts import render

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
