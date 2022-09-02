from django.forms import ModelForm
from django.http import HttpRequest, HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views import generic
from news_posts.models import NewsPosts, Comment, Notification
from news_posts.forms import CreateCommentForm
from django.db.models import Model

class CreateCommentView(LoginRequiredMixin, generic.CreateView):
    template_name: str = 'news_posts/create_comment.html'
    form_class: ModelForm = CreateCommentForm
    model: Model = Comment

    # def post(self, request):
    #     form = CreateCommentForm(request.POST)

    #     post_data = form.save(commit=False)
    #     post_data.user = get_user_model().objects.get(id=request.user.id)
    #     post_data.save()
    #     return redirect('news_posts:hot_index')

    def post(self, request: HttpRequest, *args: tuple, **kwargs: dict) ->  HttpResponseRedirect:
        # TODO:このメソッドの中にあるコメントは対象のコメントを削除した時に通知も削除されるようにするための試みであったが、できなかったので今後実装するかもしれない
        form = CreateCommentForm(request.POST)
        post_pk = self.kwargs['pk']
        post = get_object_or_404(NewsPosts, pk=post_pk)
        comment = form.save(commit=False)
        notification = Notification
        title = self.request.user.username + "が      " + post.title + "      に対してコメントした"
        # comment_notification = notification.objects.filter(title=title, message=comment.content, destination=post.user)
        comment.target = post
        comment.user = get_user_model().objects.get(id=self.request.user.id)
        comment.save()
        # comment_query = Comment.objects.filter(
        #     target=post,
        #     user=get_user_model().objects.get(id=self.request.user.id),
        #     content=comment.content
        # )
        notification.objects.create(title=title, message=comment.content, destination=post.user)
        post.latest_commented_at = timezone.now()
        post.save()

        # if not comment_query:
        #     comment_notification.delete()
        return redirect('news_posts:post_detail', pk=post_pk)

    def get_context_data(self, **kwargs: dict) -> dict:
        context = super().get_context_data(**kwargs)
        context['target_post'] = get_object_or_404(NewsPosts, pk=self.kwargs['pk'])
        return context
