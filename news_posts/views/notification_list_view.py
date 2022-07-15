from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from news_posts.models import Notification
from django.db.models import Model

class NotificationListView(LoginRequiredMixin, generic.ListView):
    model: Model = Notification
    template_name: str = 'notification/index.html'

    def get_context_data(self, **kwargs: dict) -> dict:
        context = super().get_context_data(**kwargs)
        context['notification_list'] = Notification.objects.filter(destination=self.request.user).order_by("-created_at")
        return context