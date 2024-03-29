from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from chat.models import DMRoom, DMInvite, DirectMessage
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.http import Http404, HttpRequest, HttpResponseRedirect
from django.db.models import Model
from chat.usecases.dm_room_detail_action import dm_room_detail_action


class DMRoomDetailView(LoginRequiredMixin, generic.DetailView):
    model: Model = DMRoom
    template_name: str = 'chat/dm_room_detail.html'

    def get(self, request: HttpRequest, *args: tuple, **kwargs: dict) -> HttpResponseRedirect:
        try:
            is_author = DMRoom.objects.get(id=self.kwargs['pk']).author.id
            is_addressee = DMRoom.objects.get(id=self.kwargs['pk']).addressee.id
        except DMRoom.DoesNotExist:
            raise Http404
        if is_author == request.user.id or is_addressee == request.user.id:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            return redirect('chat:home')

    def get_context_data(self, **kwargs: dict) -> dict:
        context = super().get_context_data(**kwargs)
        User = get_user_model()
        addressee_pk = DMRoom.objects.get(id=self.kwargs['pk']).author.id
        author = User.objects.get(id=self.request.user.id)
        addressee = User.objects.get(id=addressee_pk)
        dm_room_detail_action(author, addressee, self.kwargs['pk'], context)
        return context