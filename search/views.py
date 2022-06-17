from django.shortcuts import render
from django.views import generic
from communities.models import Communities
from news_posts.models import NewsPosts
from django.db.models import Sum, Q
# Create your views here.
class SearchPostsView(generic.ListView):
    template_name = 'search/index.html'

    def get_queryset(self):
        q = self.request.GET.get('q')
        # ログインユーザーのidを取得
        current_user = self.request.user.id
        object_list = NewsPosts.objects.filter(
            Q(title__icontains=q) | Q(content__icontains=q)
        ).order_by('-created_at')
        if current_user is None:
            # 未ログイン時の処理
            object_list = object_list.annotate(
                vote_count=Sum('voted_post__flag')
            ).distinct
        else:
            # ログイン時の処理
            # vote_stateにはログインユーザーの投票状態が入る
            object_list = object_list.annotate(
                vote_count=Sum('voted_post__flag'),
                vote_state=Sum('voted_post__flag',
                    filter=Q(voted_post__voted_user_id=current_user)
                )
            ).distinct
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        q = self.request.GET.get('q')
        context['communities_list'] = Communities.objects.filter(name__icontains=q).order_by('-created_at')
        context['saved_posts'] = NewsPosts.objects.filter(saved_user=self.request.user.id)
        return context
