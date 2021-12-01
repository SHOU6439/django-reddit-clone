from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
from communities.forms import CommunityForm
from .models import Communities
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class CreateCommunityView(generic.CreateView, LoginRequiredMixin):
    template_name = 'communities/create_community.html'
    model = Communities
    form_class = CommunityForm
    success_url = reverse_lazy('news_posts:index')