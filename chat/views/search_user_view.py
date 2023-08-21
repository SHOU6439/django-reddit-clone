from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from chat.usecases.search_user_action import search_user_action
from chat.usecases.chat_dm_home_list_action import chat_dm_home_list_action 




class SearchUserView(LoginRequiredMixin, generic.ListView):
    template_name: str = 'chat/search_user_result.html'

    def get_queryset(self) -> QuerySet:
        q = self.request.GET.get('q')
        object_list = search_user_action(q)
        return object_list

    def get_context_data(self, **kwargs: dict) -> dict:
        context = super().get_context_data(**kwargs)
        chat_dm_home_list_action(self.request.user, context)
        return context