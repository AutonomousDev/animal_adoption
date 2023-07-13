from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Post

# Create your views here.
class NewsDetailView(DetailView):
    model = Post
    # template_name = 'news/post_list.html'
    # context_object_name = 'posts'
    # ordering = ['-date_posted']
    # paginate_by = 5

class NewsListView(ListView):
    model = Post

