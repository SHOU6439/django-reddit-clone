from django.http import HttpRequest, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from chat.models import DMRoom, DMInvite
from django.db.models import Model
from django.contrib.auth import get_user_model
from django.shortcuts import redirect


class CreateDMRoomView(LoginRequiredMixin, generic.View):
    model: Model = DMRoom

    def get(self, request: HttpRequest, *args: tuple, **kwargs: dict) -> HttpResponseRedirect:
        User = get_user_model()
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
