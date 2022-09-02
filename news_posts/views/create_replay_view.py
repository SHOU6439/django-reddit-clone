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


class CreateReplayView(LoginRequiredMixin, generic.CreateView):
    model: Model = Replay
    form_class: ModelForm = CreateReplayForm
    template_name: str = "news_posts/create_replay.html"

    def post(self, request: HttpRequest, *args: tuple, **kwargs: dict) -> HttpResponseRedirect:
        form = self.form_class(request.POST)
        comment_pk = self.kwargs['pk']
        comment = get_object_or_404(Comment, pk=comment_pk)
        notification = Notification
        post_pk = comment.target.id
        replay = form.save(commit=False)
        # replayの対象をこのメソッド内のcomment変数に設定
        replay.target = comment
        replay.user = get_user_model().objects.get(id=self.request.user.id)
        replay.save()
        comment.replay.add(replay)
        notification.objects.create(destination=comment.user, title=self.request.user.username + "からのコメントの返信", message=replay.content)
        comment.latest_replayed_at = timezone.now()
        comment.save()
        return redirect('news_posts:post_detail', pk=post_pk)

    def get_context_data(self, **kwargs: dict) -> dict:
        context = super().get_context_data(**kwargs)
        context['target_comment'] = get_object_or_404(Comment, pk=self.kwargs['pk'])
        return context