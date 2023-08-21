from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from news_posts.models import Notification
from django.db.models import Model
from news_posts.usecases.notification_list_action import notification_list_action

class NotificationListView(LoginRequiredMixin, generic.ListView):
    model: Model = Notification
    template_name: str = 'notification/index.html'

    def get_context_data(self, **kwargs: dict) -> dict:
        context = super().get_context_data(**kwargs)
        notification_list_action(self.request.user, context)
        return context