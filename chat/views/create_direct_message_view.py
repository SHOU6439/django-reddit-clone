from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from chat.models import DMRoom, DirectMessage
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from chat.forms import CreateDirectMessageForm





class CreateDirectMessageView(LoginRequiredMixin, generic.CreateView):
    model = DirectMessage
    template_name = 'chat/dm_room_detail.html'
    form_class = CreateDirectMessageForm

    def get(self, request, *args, **kwargs):
        # formにリクエストリクエストユーザー情報を渡す
        form = self.form_class(user=request.user)
        User = get_user_model()
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        addressee_pk = self.kwargs['pk']
        User = get_user_model()
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
