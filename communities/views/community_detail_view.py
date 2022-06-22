from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.views import generic
from news_posts.models import NewsPosts, Notification
from users.models import User
from communities.models import Communities
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Q


class CommunityDetailView(LoginRequiredMixin, generic.DetailView):
    model = Communities
    template_name = 'communities/community_detail.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        # ログインユーザーのidを取得
        current_user = self.request.user.id
        queryset = NewsPosts.objects.filter(community_id=pk).order_by("-latest_commented_at", "-created_at")
        if current_user is None:
            # 未ログイン時の処理
            context['communitypost_list'] = queryset.annotate(
                like_count=Sum('liked_post__is_liked')
            )
        else:
            # ログイン時の処理
            # vote_stateにはログインユーザーの投票状態が入る
            context['communitypost_list'] = queryset.annotate(
                like_count=Sum('liked_post__is_liked'),
                like_state=Sum('liked_post__is_liked',
                    filter=Q(liked_post__liked_user_id=current_user)
                )
            )
        context['member_count'] = User.objects.filter(member=pk).count()
        context['is_joined'] = Communities.objects.filter(member=self.request.user)
        context['current_community'] = Communities.objects.get(id=pk)
        context['saved_posts'] = NewsPosts.objects.filter(saved_user=self.request.user.id)
        return context