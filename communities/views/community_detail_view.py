from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.views import generic
from news_posts.models import NewsPosts, Notification
from news_posts.utils.post_like_state_highlight import post_like_state_highlight
from users.models import User
from communities.models import Communities
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Q, Model
from communities.usecases.community_detail_action import community_detail_action


class CommunityDetailView(LoginRequiredMixin, generic.DetailView):
    model: Model = Communities
    template_name: str = 'communities/community_detail.html'

    def get_context_data(self, **kwargs: dict) -> dict:
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        # ログインユーザーのidを取得
        current_user = self.request.user.id
        post_list_name = "communitypost_list"
        queryset = NewsPosts.objects.filter(community_id=pk).order_by("-latest_commented_at", "-created_at")
        post_like_state_highlight(context, current_user, post_list_name, queryset)
        community_detail_action(self.request.user, pk, context)
        return context