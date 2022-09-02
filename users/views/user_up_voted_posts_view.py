#こちらのファイルは現在使われておりません。
from django.contrib.auth.mixins import LoginRequiredMixin
from news_posts.models import Vote
from django.contrib.auth import get_user_model
from django.views import generic
from communities.models import Communities
from django.db.models import Sum, Q



class UserUpVotedPostsView(LoginRequiredMixin, generic.DetailView):
    User = get_user_model()
    model = User
    template_name = 'users/up_voted_posts.html'
    def get_context_data(self, **kwargs: dict) -> dict:
        context = super().get_context_data(**kwargs)
        # ログインユーザーのidを取得
        current_user = self.request.user.id
        queryset = Vote.objects.filter(voted_user=self.kwargs['pk'], flag=1).order_by("-created_at")
        if current_user is None:
            # 未ログイン時の処理
            context['up_voted_posts'] = queryset.annotate(
                vote_count=Sum('flag')
            )
        else:
            # ログイン時の処理
            # vote_stateにはログインユーザーの投票状態が入る
            context['up_voted_posts'] = queryset.annotate(
                vote_count=Sum('flag'),
                vote_state=Sum('flag',
                    filter=Q(voted_user_id=current_user)
                )
            )
        context['communities_list'] = Communities.objects.filter(member=self.kwargs['pk']).order_by("-created_at")
        return context
