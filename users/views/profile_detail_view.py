from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from communities.models import Communities
from news_posts.models import NewsPosts
from users.models import User
from django.db.models import Sum, Q

class ProfileDetailView(LoginRequiredMixin ,generic.DetailView):
    model = User
    template_name = 'users/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ログインユーザーのidを取得
        current_user = self.request.user.id
        queryset = NewsPosts.objects.filter(user_id=self.kwargs['pk']).order_by("-created_at")
        if current_user is None:
            # 未ログイン時の処理
            context['userpost_list'] = queryset.annotate(
                vote_count=Sum('voted_post__flag')
            )
        else:
            # ログイン時の処理
            # vote_stateにはログインユーザーの投票状態が入る
            context['userpost_list'] = queryset.annotate(
                vote_count=Sum('voted_post__flag'),
                vote_state=Sum('voted_post__flag',
                    filter=Q(voted_post__voted_user_id=current_user)
                )
            )
        context['communities_list'] = Communities.objects.filter(member=self.kwargs['pk']).order_by("-created_at")
        context['saved_posts'] = NewsPosts.objects.filter(saved_user=self.request.user.id)
        return context