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


class CommunityDetailView(LoginRequiredMixin, generic.DetailView):
    model = Communities
    template_name = 'communities/community_detail.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['communitypost_list'] = NewsPosts.objects.filter(community_id=pk).order_by("-latest_commented_at", "-created_at")
        context['member_count'] = User.objects.filter(member=pk).count()
        context['is_joined'] = Communities.objects.filter(member=self.request.user)
        context['current_community'] = Communities.objects.get(id=pk)
        context['saved_posts'] = NewsPosts.objects.filter(saved_user=self.request.user.id)
        return context