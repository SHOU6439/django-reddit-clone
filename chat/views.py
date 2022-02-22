from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from chat.models import DMInvite, DMRoom, DirectMessage
from news_posts.models import Notification
from users.models import User
# Create your views here.

# class CreateDMChatRoomView(LoginRequiredMixin, generic.View):
#     model = DirectMessage
#     template_name = "chat/create_dm_chat_room.html"

class ChatHomeView(LoginRequiredMixin, generic.ListView):
    model = DMRoom
    template_name = 'chat/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dm_invites'] = DMInvite.objects.filter(received_user=self.request.user.id).order_by("-created_at")
        context['dm_rooms'] = DMRoom.objects.filter(author=self.request.user.id).order_by("-created_at")
        # TODO:のちにグループチャットを追加した際にグループチャットの一覧のコンテキストも渡す
        return context


class ChatDMHomeView(LoginRequiredMixin, generic.ListView):
    model = DMRoom
    template_name = 'chat/dm_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dm_invites'] = DMInvite.objects.filter(received_user=self.request.user.id).order_by("-created_at")
        context['dm_rooms'] = DMRoom.objects.filter(author=self.request.user.id).order_by("-created_at")
        return context


class SearchUserView(LoginRequiredMixin, generic.ListView):
    template_name = 'chat/search_user.html'

    def get_queryset(self):
        q = self.request.GET.get('q')
        object_list = User.objects.filter(username__icontains=q).order_by('-created_at')
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dm_invites'] = DMInvite.objects.filter(received_user=self.request.user.id).order_by("-created_at")
        context['dm_rooms'] = DMRoom.objects.filter(author=self.request.user.id).order_by("-created_at")
        # TODO:のちにグループチャットを追加した際にグループチャットの一覧のコンテキストも渡す
        return context


class CreateDMRoomView(LoginRequiredMixin, generic.View):
    model = DMRoom

    def get(self, request, *args, **kwargs):
        addressee_pk = self.kwargs['pk']
        author = User.objects.get(id=request.user.id)
        addressee = User.objects.get(id=addressee_pk)
        author_room = DMRoom.objects.filter(author=author, addressee=addressee)
        addressee_room = DMRoom.objects.filter(author=addressee, addressee=author)
        if not author_room:
            # author側でDMルームを作成
            DMRoom.objects.create(author=author, addressee=addressee)

        dm_invite = DMInvite.objects.filter(invited_user=author, received_user=addressee)
        dm_receive = DMInvite.objects.filter(invited_user=addressee, received_user=author)
        if not dm_invite:
            # DM招待を作成
            get_author_room = DMRoom.objects.filter(author=author, addressee=addressee).first()
            DMInvite.objects.create(room=get_author_room, invited_user=author, received_user=addressee)
            if author_room and addressee_room:
                # DMルームが既に双方に存在する場合既にDM招待は承認されてるので削除。
                dm_invite.delete()
        if dm_receive:
            # 受信する側からもDM招待を送られた場合は双方のDM招待を削除し、そのまま双方にDMルームを作成。実質DM招待の承認と同じ動きをします。
            dm_invite.delete()
            dm_receive.delete()
        author_room_pk = DMRoom.objects.filter(author=author, addressee=addressee).first().id
        return redirect('chat:dm_room_detail', pk=author_room_pk)

class DMRoomDetailView(LoginRequiredMixin, generic.DetailView):
    model = DMRoom
    template_name = 'chat/dm_room_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_room'] = DMRoom.objects.get(id=self.kwargs['pk'])
        context['dm_list'] = DirectMessage.objects.filter(room=self.kwargs['pk'])
        context['dm_invites'] = DMInvite.objects.filter(received_user=self.request.user.id).order_by("-created_at")
        context['dm_rooms'] = DMRoom.objects.filter(author=self.request.user.id).order_by("-created_at")
        return context
