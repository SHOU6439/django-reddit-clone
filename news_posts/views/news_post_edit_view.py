from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.urls.base import reverse
from django.views import generic
from news_posts.models import NewsPosts
from news_posts.forms import NewsPostEditForm
from django.db.models import Model
from news_posts.usecases.get_news_post_edit_form_action import get_news_post_edit_form_action


class NewsPostEditView(LoginRequiredMixin, generic.UpdateView):
    model: Model = NewsPosts
    form_class: ModelForm = NewsPostEditForm
    template_name: str = 'news_posts/post_edit.html'
    def get_success_url(self):
        post_pk = self.kwargs['pk']
        return reverse('news_posts:post_detail', kwargs={'pk': post_pk})

    def get_context_data(self, **kwargs: dict) -> dict:
        post_pk = self.kwargs['pk']
        post = NewsPosts.objects.get(id=post_pk)
        context = super().get_context_data(**kwargs)
        get_news_post_edit_form_action(self.request.user, post, context)
        return context