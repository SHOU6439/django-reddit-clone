from django.shortcuts import render
from django.views import generic
from .models import NewsPosts
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'news_posts/index.html'

    def get_queryset(self):
        return NewsPosts.objects.all()

def index(request):
    return render(request, 'news_posts/index.html')