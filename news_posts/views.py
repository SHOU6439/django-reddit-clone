from typing import ContextManager
from urllib.parse import urlencode
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import SuccessURLAllowedHostsMixin
from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.base import TemplateView
from communities.models import Communities
from users.models import User
from .models import NewsPosts
from .forms import CreatePostForm
# Create your views here.

class IndexView(generic.ListView):
    model = NewsPosts
    template_name = 'news_posts/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = NewsPosts.objects.order_by('-created_at')
        context['communities_list'] = Communities.objects.order_by('-created_at')
        return context

class CreatePostView(LoginRequiredMixin, generic.CreateView):
    model = NewsPosts
    form_class = CreatePostForm
    template_name = 'news_posts/create_post.html'
    success_url = reverse_lazy('news_posts:index')
    def post(self, request):
        form = CreatePostForm(request.POST)

        get_user_id = form.save(commit=False)
        get_user_id.user = get_user_model().objects.get(id=request.user.id)
        get_user_id.save()
        return redirect('news_posts:index')

    def get_queryset(self):
        return Communities.objects.all()


class DeletePostView(LoginRequiredMixin, generic.DeleteView):
    model = NewsPosts
    success_url = reverse_lazy('news_posts:index')

class DeleteLoginUserPostView(LoginRequiredMixin, generic.DeleteView):
    model = NewsPosts
    def get_success_url(self):
        return reverse('users:detail', kwargs={'pk': self.request.user.id})

class NewsPostDetailView(LoginRequiredMixin, generic.DetailView):
    model = NewsPosts
    template_name = 'news_posts/post_detail.html'