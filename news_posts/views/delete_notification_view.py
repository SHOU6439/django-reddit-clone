from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse
from django.views import generic
from news_posts.models import Notification
from django.db.models import Model

class DeleteNotificationView(LoginRequiredMixin, generic.DeleteView):
    model: Model = Notification
    def get_success_url(self):
        return reverse('news_posts:notification', kwargs={'pk': self.request.user.id})