from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls.base import reverse, reverse_lazy
from django.views import generic
from news_posts.models import Comment, Replay
from django.db.models import Model

class DeleteReplayView(LoginRequiredMixin, generic.DeleteView):
    model: Model = Replay
    success_url = reverse_lazy('news_posts:hot_index')
    def get_success_url(self):
        # replayの対象であるコメントの対象であるポストのpkを取得する
        replay_pk = self.kwargs['pk']
        replay = get_object_or_404(Replay, pk=replay_pk)
        comment_pk = replay.target.id
        comment = get_object_or_404(Comment, pk=comment_pk)
        post_pk = comment.target.id
        return reverse('news_posts:post_detail', kwargs={'pk': post_pk})
