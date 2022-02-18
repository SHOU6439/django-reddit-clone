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
        if DMRoom.objects.filter(author=author, addressee=addressee).count() == 0:
            DMRoom.objects.create(author=author, addressee=addressee)
        # else:
        #     TODO:DMのdetail画面が作成されたらdetail画面に飛ぶようにする

        # dm_invite = Notification.objects.filter(title=author.username + "からのDM招待", message="承認する場合は相手にDMを送ってみてください!", destination=addressee)
        # if not dm_invite:
        #     Notification.objects.create(title=author.username + "からのDM招待", message="承認する場合は相手にDMを送ってみてください!", destination=addressee)
        return redirect('chat:home')
