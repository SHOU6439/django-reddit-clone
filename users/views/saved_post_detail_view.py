from django.contrib.auth.mixins import LoginRequiredMixin
from news_posts.models import NewsPosts
from django.contrib.auth import get_user_model
from django.views import generic
from communities.models import Communities
from django.db.models import Sum, Q, Model


class SavedPostDetailView(LoginRequiredMixin, generic.DetailView):
    User: Model = get_user_model()
    model = User
    template_name: str = 'users/saved_post_list.html'

    def get_context_data(self, **kwargs: dict) -> dict:
        context = super().get_context_data(**kwargs)
        # ログインユーザーのidを取得
        current_user = self.request.user.id
        #　ソートしなくても保存した順になっているのでorder_byを使用していない
        queryset = NewsPosts.objects.filter(saved_user=self.kwargs['pk'])
        if current_user is None:
            # 未ログイン時の処理
            context['saved_posts'] = queryset.annotate(
                like_count=Sum('liked_post__is_liked')
            )
        else:
            # ログイン時の処理
            # vote_stateにはログインユーザーの投票状態が入る
            context['saved_posts'] = queryset.annotate(
                like_count=Sum('liked_post__is_liked'),
                like_state=Sum('liked_post__is_liked',
                    filter=Q(liked_post__liked_user_id=current_user)
                )
            )
        context['communities_list'] = Communities.objects.filter(member=self.kwargs['pk']).order_by("-created_at")
        return context