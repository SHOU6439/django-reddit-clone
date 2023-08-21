from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from communities.models import Communities
from news_posts.models import NewsPosts
from news_posts.utils.post_like_state_highlight import post_like_state_highlight
from users.models import User
from django.db.models import Sum, Q, Model

class ProfileDetailView(LoginRequiredMixin ,generic.DetailView):
    model: Model = User
    template_name: str = 'users/profile_detail.html'

    def get_context_data(self, **kwargs: dict) -> dict:
        context = super().get_context_data(**kwargs)
        # ログインユーザーのidを取得
        current_user = self.request.user.id
        post_list_name = "userpost_list"
        queryset = NewsPosts.objects.filter(user_id=self.kwargs['pk']).order_by("-created_at")
        post_like_state_highlight(context, current_user, post_list_name, queryset)
        context['communities_list'] = Communities.objects.filter(member=self.kwargs['pk']).order_by("-created_at")
        context['saved_posts'] = NewsPosts.objects.filter(saved_user=self.request.user.id)
        return context