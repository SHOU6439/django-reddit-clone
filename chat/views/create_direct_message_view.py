from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.db.models import Model
from django.forms import ModelForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from chat.models import DMRoom, DirectMessage
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from chat.forms import CreateDirectMessageForm
from chat.usecases.post_direct_message_action import post_direct_message_action





class CreateDirectMessageView(LoginRequiredMixin, generic.View):
    model: Model = DirectMessage
    template_name: str = 'chat/dm_room_detail.html'
    form_class: ModelForm = CreateDirectMessageForm

    def get(self, request: HttpRequest, *args: tuple, **kwargs: dict) -> HttpResponse:
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

    def post(self, request: HttpRequest, *args: tuple, **kwargs: dict) -> HttpResponseRedirect:
        form = self.form_class(request.POST)
        addressee_pk = self.kwargs['pk']
        User = get_user_model()
        author = User.objects.get(id=self.request.user.id)
        addressee = User.objects.get(id=addressee_pk)
        author_room = DMRoom.objects.get(author=author, addressee=addressee)
        addressee_room = DMRoom.objects.filter(author=addressee, addressee=author)
        author_room_pk = DMRoom.objects.get(
            author=author,
            addressee=addressee
        ).id
        post_direct_message_action(request, form, author_room, addressee_room, addressee_pk)
        return redirect('chat:dm_room_detail', pk=author_room_pk)
