from django.contrib.auth.mixins import LoginRequiredMixin
from news_posts.models import NewsPosts
from django.contrib.auth import get_user_model
from django.views import generic
from communities.models import Communities
from django.db.models import Sum, Q


class SavedPostDetailView(LoginRequiredMixin, generic.DetailView):
    User = get_user_model()
    model = User
    template_name = 'users/saved_post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ログインユーザーのidを取得
        current_user = self.request.user.id
        #　ソートしなくても保存した順になっているのでorder_byを使用していない
        queryset = NewsPosts.objects.filter(saved_user=self.kwargs['pk'])
        if current_user is None:
            # 未ログイン時の処理
            context['saved_posts'] = queryset.annotate(
                vote_count=Sum('voted_post__flag')
            )
        else:
            # ログイン時の処理
            # vote_stateにはログインユーザーの投票状態が入る
            context['saved_posts'] = queryset.annotate(
                vote_count=Sum('voted_post__flag'),
                vote_state=Sum('voted_post__flag',
                    filter=Q(voted_post__voted_user_id=current_user)
                )
            )
        context['communities_list'] = Communities.objects.filter(member=self.kwargs['pk']).order_by("-created_at")
        return context