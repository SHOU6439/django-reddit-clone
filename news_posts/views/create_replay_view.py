from django.forms import ModelForm
from django.http import HttpRequest, HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views import generic
from news_posts.models import Comment, Notification, Replay
from news_posts.forms import CreateReplayForm
from django.db.models import Model
from news_posts.usecases.create_replay_action import create_replay_action


class CreateReplayView(LoginRequiredMixin, generic.CreateView):
    model: Model = Replay
    form_class: ModelForm = CreateReplayForm
    template_name: str = "news_posts/create_replay.html"

    def post(self, request: HttpRequest, *args: tuple, **kwargs: dict) -> HttpResponseRedirect:
        form = self.form_class(request.POST)
        comment_pk = self.kwargs['pk']
        if form.is_valid():
            comment = create_replay_action(request.user, form, comment_pk)
            post_pk = comment.target.id
            return redirect('news_posts:post_detail', pk=post_pk)
        return redirect('news_posts:create_replay', pk=comment_pk)
        

    def get_context_data(self, **kwargs: dict) -> dict:
        context = super().get_context_data(**kwargs)
        context['target_comment'] = get_object_or_404(Comment, pk=self.kwargs['pk'])
        return context