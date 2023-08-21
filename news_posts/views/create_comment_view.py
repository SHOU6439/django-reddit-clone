from django.forms import ModelForm
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views import generic
from news_posts.models import NewsPosts, Comment
from news_posts.forms import CreateCommentForm
from django.db.models import Model
from news_posts.usecases.create_comment_action import create_comment_action

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
        if form.is_valid():
            create_comment_action(request.user, form, post_pk)
            return redirect('news_posts:post_detail', pk=post_pk)
        return redirect('news_posts:create_comment', pk=post_pk)

    def get_context_data(self, **kwargs: dict) -> dict:
        context = super().get_context_data(**kwargs)
        context['target_post'] = get_object_or_404(NewsPosts, pk=self.kwargs['pk'])
        return context
