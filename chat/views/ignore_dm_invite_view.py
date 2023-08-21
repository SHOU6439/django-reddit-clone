from django.http import HttpRequest, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from chat.models import DMInvite
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.db.models import Model
from chat.usecases.ignore_dm_invite_action import ignore_dm_invite_action


class IgnoreDMInviteView(LoginRequiredMixin, generic.View):
    model: Model = DMInvite

    def get(self, request: HttpRequest, *args: tuple, **kwargs: dict) -> HttpResponseRedirect:
        addressee_pk = self.kwargs['pk']
        User = get_user_model()
        author = User.objects.get(id=request.user.id)
        addressee = User.objects.get(id=addressee_pk)
        dm_invite = DMInvite.objects.filter(
            invited_user=addressee,
            received_user=author
        )
        ignore_dm_invite_action(dm_invite, author, addressee)
        return redirect('chat:home')
