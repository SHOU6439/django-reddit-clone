from django.shortcuts import render
from django.views import generic
from communities.models import Communities
from news_posts.models import NewsPosts
# Create your views here.
class SearchView(generic.ListView):
    template_name = 'search/index.html'

    def get_queryset(self):
        q = self.request.GET.get('q')
        return NewsPosts.objects.filter(title__contains=q)