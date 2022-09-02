from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse
from django.views import generic
from news_posts.models import NewsPosts
from django.db.models import Model

class DeleteLoginUserPostView(LoginRequiredMixin, generic.DeleteView):
    model: Model = NewsPosts
    def get_success_url(self) -> str:
        return reverse('users:detail', kwargs={'pk': self.request.user.id})