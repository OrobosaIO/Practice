from pdb import post_mortem
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

from base.models import Post

#def home(request):
#    return render(request, 'base/home.html')

class HomeView(ListView):
    model = Post
    template_name = 'base/home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'base/article_details.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'base/add_post.html'
    fields = '__all__'
    #fields = ('title', 'body')
