from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from chat.models import DMRoom, DMInvite

class ChatHomeView(LoginRequiredMixin, generic.ListView):
    model = DMRoom
    template_name = 'chat/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dm_invites'] = DMInvite.objects.filter(received_user=self.request.user.id).order_by("-created_at")
        context['dm_rooms'] = DMRoom.objects.filter(author=self.request.user.id).order_by("-created_at")
        # TODO:のちにグループチャットを追加した際にグループチャットの一覧のコンテキストも渡す
        return context
