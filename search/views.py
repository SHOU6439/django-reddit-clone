from django.shortcuts import render
from django.views import generic
from communities.models import Communities
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'search/index.html'

    def get_queryset(self):
        q = self.request.GET.get('q')
        return Communities.objects.filter(name__contains=q)