from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.views import generic
from news_posts.models import NewsPosts


class DeletePostView(LoginRequiredMixin, generic.DeleteView):
    model = NewsPosts
    success_url = reverse_lazy('news_posts:index')