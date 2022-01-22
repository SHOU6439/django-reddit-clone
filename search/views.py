from django.shortcuts import render
from django.views import generic
from communities.models import Communities
from news_posts.models import NewsPosts
from django.db.models import Q
# Create your views here.
class SearchView(generic.ListView):
    template_name = 'search/index.html'

    def get_queryset(self):
        q = self.request.GET.get('q')
        object_list = NewsPosts.objects.filter(
            Q(title__icontains=q) | Q(content__icontains=q)
        ).order_by('-created_at').distinct
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        q = self.request.GET.get('q')
        context['communities_list'] = Communities.objects.filter(name__icontains=q).order_by('-created_at')
        return context
