from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import ListView, DetailView
from .models import Post



class PostsView(ListView):
    queryset=Post.objects.all()
    template_name='blog/posts.html'
    context_object_name='posts'


class SinglePostView(DetailView):
    model=Post
    template_name='blog/post.html'
    context_object_name='post'

    def get_object(self):
        post=get_object_or_404(Post, pk=self.kwargs['id'], slug__iexact=self.kwargs['slug'])
        return post

    
