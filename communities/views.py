from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.views import generic
from communities.forms import CommunityForm
from news_posts.models import NewsPosts, Notification
from users.models import User
from .models import Communities
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
# Create your views here.
class CreateCommunityView(LoginRequiredMixin, generic.CreateView):
    template_name = 'communities/create_community.html'
    model = Communities
    form_class = CommunityForm
    success_url = reverse_lazy('news_posts:index')
    def post(self, request):
        form = CommunityForm(request.POST)

        post_data = form.save(commit=False)
        post_data.admin = get_user_model().objects.get(id=request.user.id)
        post_data.save()
        community = Communities.objects.get(name=post_data.name)
        # adminがコミュニティを作ったら自動的にadminはmemberに追加する
        community.member.add(request.user.id)
        community.save()
        return redirect('news_posts:index')

class CommunityDetailView(LoginRequiredMixin, generic.DetailView):
    model = Communities
    template_name = 'communities/community_detail.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['communitypost_list'] = NewsPosts.objects.filter(community_id=pk).order_by("-created_at")
        context['member_count'] = User.objects.filter(member=pk).count()
        context['is_joined'] = Communities.objects.filter(member=self.request.user)
        context['current_community'] = Communities.objects.get(id=pk)
        context['saved_posts'] = NewsPosts.objects.filter(saved_user=self.request.user.id)
        return context

@login_required
def join(request, pk):
    community = Communities.objects.get(pk=pk)
    notification = Notification
    message = request.user.username + "が      " + community.name + "      に加入した!"
    join_notification = notification.objects.filter(title="communityメンバー加入通知", message=message, destination=community.admin)
    community.member.add(request.user.id)
    community.save()
    # 直近にcommunityをleaveした場合にjoin_notificationを作り直す
    if join_notification:
        join_notification.delete()
    if not join_notification:
        notification.objects.create(title="communityメンバー加入通知", message=message, destination=community.admin)
    return redirect('communities:detail', pk=pk)

login_required
def leave(request, pk):
    community = Communities.objects.get(pk=pk)
    notification = Notification
    message = request.user.username + "が      " + community.name + "      を離脱した..."
    leave_notification = notification.objects.filter(title="communityメンバー離脱通知", message=message, destination=community.admin)
    community.member.remove(request.user.id)
    community.save()
    # 直近にcommunityをjoinした場合にleave_notificationを作り直す
    if leave_notification:
        leave_notification.delete()
    if not leave_notification:
        notification.objects.create(title="communityメンバー離脱通知", message=message, destination=community.admin)
    return redirect('communities:detail', pk=pk)