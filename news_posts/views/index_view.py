from django.db.models import Sum, Q
from django.views import generic
from communities.models import Communities
from news_posts.models import NewsPosts, Vote


class IndexView(generic.ListView):
    model = NewsPosts
    template_name = 'news_posts/index/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ログインユーザーのidを取得
        current_user = self.request.user.id
        queryset = NewsPosts.objects.order_by('-created_at')
        if current_user is None:
            # 未ログイン時の処理
            context['post_list'] = queryset.annotate(
                vote_count=Sum('voted_post__flag')
            )
        else:
            # ログイン時の処理
            # vote_stateにはログインユーザーの投票状態が入る
            context['post_list'] = queryset.annotate(
                vote_count=Sum('voted_post__flag'),
                vote_state=Sum('voted_post__flag',
                    filter=Q(voted_post__voted_user_id=current_user)
                )
            )

        context['vote_list'] = Vote.objects.filter(voted_user_id=self.request.user.id)
        context['communities_list'] = Communities.objects.order_by('-created_at')
        context['saved_posts'] = NewsPosts.objects.filter(saved_user=self.request.user.id)
        return context