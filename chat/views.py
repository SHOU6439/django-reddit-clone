from email import message
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from chat.models import DMInvite, DMRoom, DirectMessage
from news_posts.models import Notification
from users.models import User
from .forms import CreateDirectMessageForm
from django.contrib.auth import get_user_model
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
    template_name = 'chat/search_user_result.html'

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
        author_room_pk = DMRoom.objects.filter(
            author=author, addressee=addressee
        ).first().id
        return redirect('chat:dm_room_detail', pk=author_room_pk)

class DMRoomDetailView(LoginRequiredMixin, generic.DetailView):
    model = DMRoom
    template_name = 'chat/dm_room_detail.html'

    def get(self, request, *args, **kwargs):
        is_author = DMRoom.objects.get(id=self.kwargs['pk']).author.id
        is_addressee = DMRoom.objects.get(id=self.kwargs['pk']).addressee.id
        if is_author == self.request.user.id or is_addressee == self.request.user.id:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            return redirect('chat:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        addressee_pk = DMRoom.objects.get(id=self.kwargs['pk']).author.id
        author = User.objects.get(id=self.request.user.id)
        addressee = User.objects.get(id=addressee_pk)
        context['current_invite'] = DMInvite.objects.filter(invited_user=addressee, received_user=author)
        context['current_room'] = DMRoom.objects.get(id=self.kwargs['pk'])
        context['dm_list'] = DirectMessage.objects.filter(room=self.kwargs['pk'])
        context['dm_invites'] = DMInvite.objects.filter(received_user=self.request.user.id).order_by("-created_at")
        context['dm_rooms'] = DMRoom.objects.filter(author=self.request.user.id).order_by("-created_at")
        return context

class AcceptDMInviteView(LoginRequiredMixin, generic.View):
    model = DMInvite

    def get(self, request, *args, **kwargs):
        addressee_pk = self.kwargs['pk']
        author = User.objects.get(id=request.user.id)
        addressee = User.objects.get(id=addressee_pk)
        dm_invite = DMInvite.objects.filter(
            invited_user=addressee,
            received_user=author
        )
        dm_invite.accept = True
        dm_invite.delete()
        if not DMRoom.objects.filter(author=author, addressee=addressee):
            DMRoom.objects.create(author=author, addressee=addressee)
            addressee_room_messages = DirectMessage.objects.filter(
                room=DMRoom.objects.get(author=addressee, addressee=author),
            )
            if addressee_room_messages:
                message_storage = []
                for message in addressee_room_messages:
                    message_storage.append(DirectMessage(
                        room=DMRoom.objects.get(author=author, addressee=addressee),
                        sender=message.sender,
                        content=message.content,
                        created_at=message.created_at,
                    ))
                DirectMessage.objects.bulk_create(
                    message_storage
                )
        author_room_pk = DMRoom.objects.get(
            author=author,
            addressee=addressee
        ).id
        return redirect('chat:dm_room_detail', pk=author_room_pk)

class IgnoreDMInviteView(LoginRequiredMixin, generic.View):
    model = DMInvite

    def get(self, request, *args, **kwargs):
        addressee_pk = self.kwargs['pk']
        author = User.objects.get(id=request.user.id)
        addressee = User.objects.get(id=addressee_pk)
        dm_invite = DMInvite.objects.filter(
            invited_user=addressee,
            received_user=author
        )
        dm_invite.ignore = True
        if not DMRoom.objects.filter(author=author, addressee=addressee):
            dm_invite.delete()
            DMRoom.objects.filter(
                author=addressee,
                addressee=author
            ).delete()
        return redirect('chat:home')



class CreateDirectMessageView(LoginRequiredMixin, generic.CreateView):
    model = DirectMessage
    template_name = 'chat/dm_room_detail.html'
    form_class = CreateDirectMessageForm

    def get(self, request, *args, **kwargs):
        # formにリクエストリクエストユーザー情報を渡す
        form = self.form_class(user=request.user)
        addressee_pk = self.kwargs['pk']
        author = User.objects.get(id=self.request.user.id)
        addressee = User.objects.get(id=addressee_pk)
        author_room_pk = DMRoom.objects.get(
            author=author,
            addressee=addressee
        ).id
        return render(request, self.template_name, {'form': form, 'pk': author_room_pk})

    # def post(self, request):
    #     form = CreateDirectMessageForm(data=request.POST)
    #     addressee_pk = self.kwargs['pk']
    #     author = User.objects.get(id=self.request.user.id)
    #     addressee = User.objects.get(id=addressee_pk)
    #     if form.is_valid():
    #         post_data = form.save(commit=False)
    #         post_data.save()
    #         author_room_pk = DMRoom.objects.get(
    #             author=author,
    #             addressee=addressee
    #         ).id
    #     return redirect('chat:dm_room_detail', pk=author_room_pk)

    def form_valid(self, form):
        addressee_pk = self.kwargs['pk']
        author = User.objects.get(id=self.request.user.id)
        addressee = User.objects.get(id=addressee_pk)
        author_room = DMRoom.objects.get(author=author, addressee=addressee)
        addressee_room = DMRoom.objects.filter(author=addressee, addressee=author)
        post_data = form.save(commit=False)
        post_data.sender = get_user_model().objects.get(id=self.request.user.id)
        post_data.room = author_room
        post_data.save()
        if addressee_room:
            get_addressee_room = DMRoom.objects.get(author=addressee, addressee=author)
            DirectMessage.objects.create(room=get_addressee_room, sender=author, content=post_data.content)
        author_room_pk = DMRoom.objects.get(
            author=author,
            addressee=addressee
        ).id
        return redirect('chat:dm_room_detail', pk=author_room_pk)


