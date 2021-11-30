from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
from .models import NewsPosts
from .forms import CreatePostForm
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'news_posts/index.html'

    def get_queryset(self):
        return NewsPosts.objects.all()

class CreatePostView(generic.CreateView):
    model = NewsPosts
    form_class = CreatePostForm
    template_name = 'news_posts/create_post.html'
    success_url = reverse_lazy('news_posts:index')


