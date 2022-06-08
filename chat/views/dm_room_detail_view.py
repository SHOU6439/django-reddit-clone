from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from chat.models import DMRoom, DMInvite, DirectMessage
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.http import Http404


class DMRoomDetailView(LoginRequiredMixin, generic.DetailView):
    model = DMRoom
    template_name = 'chat/dm_room_detail.html'

    def get(self, request, *args, **kwargs):
        try:
            is_author = DMRoom.objects.get(id=self.kwargs['pk']).author.id
            is_addressee = DMRoom.objects.get(id=self.kwargs['pk']).addressee.id
        except DMRoom.DoesNotExist:
            raise Http404
        if is_author == self.request.user.id or is_addressee == self.request.user.id:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            return redirect('chat:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        User = get_user_model()
        addressee_pk = DMRoom.objects.get(id=self.kwargs['pk']).author.id
        author = User.objects.get(id=self.request.user.id)
        addressee = User.objects.get(id=addressee_pk)
        context['current_invite'] = DMInvite.objects.filter(invited_user=addressee, received_user=author)
        context['current_room'] = DMRoom.objects.get(id=self.kwargs['pk'])
        context['dm_list'] = DirectMessage.objects.filter(room=self.kwargs['pk'])
        context['dm_invites'] = DMInvite.objects.filter(received_user=self.request.user.id).order_by("-created_at")
        context['dm_rooms'] = DMRoom.objects.filter(author=self.request.user.id).order_by("-created_at")
        return context