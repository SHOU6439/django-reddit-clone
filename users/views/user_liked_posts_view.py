from django.contrib.auth.mixins import LoginRequiredMixin
from news_posts.models import Like
from django.contrib.auth import get_user_model
from django.views import generic
from communities.models import Communities
from django.db.models import Sum, Q, Model
from news_posts.utils.like_state_highlight import like_state_highlight



class UserLikedPostsView(LoginRequiredMixin, generic.DetailView):
    User: Model = get_user_model()
    model = User
    template_name: str = 'users/liked_posts.html'
    def get_context_data(self, **kwargs: dict) -> dict:
        context = super().get_context_data(**kwargs)
        # ログインユーザーのidを取得
        current_user = self.request.user.id
        post_list_name = "liked_posts"
        queryset = Like.objects.filter(liked_user=self.kwargs['pk'], is_liked=True).order_by("-created_at")
        like_state_highlight(context, current_user, post_list_name, queryset)
        context['communities_list'] = Communities.objects.filter(member=self.kwargs['pk']).order_by("-created_at")
        return context
