from django.http import HttpRequest, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from chat.models import DMRoom, DMInvite
from django.db.models import Model
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from chat.usecases.create_dm_room_action import create_dm_room_acton


class CreateDMRoomView(LoginRequiredMixin, generic.View):
    model: Model = DMRoom

    def get(self, request: HttpRequest, *args: tuple, **kwargs: dict) -> HttpResponseRedirect:
        User = get_user_model()
        addressee_pk = self.kwargs['pk']
        author = User.objects.get(id=request.user.id)
        addressee = User.objects.get(id=addressee_pk)
        author_room = DMRoom.objects.filter(author=author, addressee=addressee)
        addressee_room = DMRoom.objects.filter(author=addressee, addressee=author)
        create_dm_room_acton(author, addressee, author_room, addressee_room)
        author_room_pk = DMRoom.objects.filter(
            author=author, addressee=addressee
        ).first().id
        return redirect('chat:dm_room_detail', pk=author_room_pk)
