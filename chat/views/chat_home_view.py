from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from chat.models import DMRoom
from django.db.models import Model
from chat.usecases.chat_dm_home_list_action import chat_dm_home_list_action

class ChatHomeView(LoginRequiredMixin, generic.ListView):
    model: Model = DMRoom
    template_name: str = 'chat/home.html'

    def get_context_data(self, **kwargs: dict) -> dict:
        context = super().get_context_data(**kwargs)
        chat_dm_home_list_action(self.request.user, context)
        return context
