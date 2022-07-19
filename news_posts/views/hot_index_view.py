from multiprocessing import context
from django.db.models import Sum, Q
from django.views import generic
from communities.models import Communities
from news_posts.models import NewsPosts
from news_posts.usecases.post_like_state_highlight import post_like_state_highlight
from .new_index_view import NewIndexView


class HotIndexView(NewIndexView):
    template_name: str = 'news_posts/index/hot_index.html'

    def get_context_data(self, **kwargs: dict) -> dict:
        context = super().get_context_data(**kwargs)
        current_user = self.request.user.id
        post_list_name = "post_list"
        queryset = NewsPosts.objects.order_by("-latest_commented_at", "-created_at")
        post_like_state_highlight(context, current_user, post_list_name, queryset)
        # context['vote_list'] = Vote.objects.filter(voted_user_id=self.request.user.id)
        context['communities_list'] = Communities.objects.order_by('-latest_posted_at', '-created_at')
        context['saved_posts'] = NewsPosts.objects.filter(saved_user=self.request.user.id)
        return context