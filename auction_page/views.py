from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Auction_Post
from django.shortcuts import render


class PostList(ListView):
    model = Auction_Post
    ordering = '-pk'
    template_name = 'auction_page/auction_post_list.html'


class PostDetail(DetailView):
    model = Auction_Post

