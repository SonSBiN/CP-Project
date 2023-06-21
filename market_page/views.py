from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
import json

class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'market_page/post_list.html'


class PostDetail(DetailView):
    model = Post


def index(request):
    return render(
        request,
        'chat/room.html',
        {}
    )

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content', 'head_image',]