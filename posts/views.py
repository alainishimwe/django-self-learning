from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
# learning github

class PostList(generic.ListView):
    queryset = Post.objects.filter.order_by('created_on')
    template_name = 'index.html'

class CommentList(generic.CreateListView):
    queryset = Post.objects.all()
    template_name = 'index.html'