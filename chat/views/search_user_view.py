from django.http import QueryDict
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from chat.models import DMRoom, DMInvite
from django.contrib.auth import get_user_model
from django.db.models.query import QuerySet




class SearchUserView(LoginRequiredMixin, generic.ListView):
    template_name: str = 'chat/search_user_result.html'

    def get_queryset(self) -> QuerySet:
        q = self.request.GET.get('q')
        object_list = get_user_model().objects.filter(username__icontains=q).order_by('-created_at')
        return object_list

    def get_context_data(self, **kwargs: dict) -> dict:
        context = super().get_context_data(**kwargs)
        context['dm_invites'] = DMInvite.objects.filter(received_user=self.request.user.id).order_by("-created_at")
        context['dm_rooms'] = DMRoom.objects.filter(author=self.request.user.id).order_by("-created_at")
        # TODO:のちにグループチャットを追加した際にグループチャットの一覧のコンテキストも渡す
        return context