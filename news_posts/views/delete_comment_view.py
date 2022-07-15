from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse
from django.views import generic
from news_posts.models import Comment
from django.shortcuts import get_object_or_404
from django.db.models import Model

class DeleteCommentView(LoginRequiredMixin, generic.DeleteView):
    model: Model = Comment

    def get_success_url(self):
        comment_pk = self.kwargs['pk']
        comment = get_object_or_404(Comment, pk=comment_pk)
        post_pk = comment.target.id
        return reverse('news_posts:post_detail', kwargs={'pk': post_pk})
