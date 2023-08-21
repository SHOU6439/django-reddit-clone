from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from news_posts.models import NewsPosts
from news_posts.usecases.news_post_detail_action import news_post_detail_action
from django.db.models import Model

class NewsPostDetailView(LoginRequiredMixin, generic.DetailView):
    model: Model = NewsPosts
    template_name: str = 'news_posts/post_detail.html'
    def get_context_data(self, **kwargs: dict) -> dict:
        post_pk = self.kwargs['pk']
        post = NewsPosts.objects.get(id=post_pk)
        context = super().get_context_data(**kwargs)
        news_post_detail_action(self.request.user, post, context)
        return context