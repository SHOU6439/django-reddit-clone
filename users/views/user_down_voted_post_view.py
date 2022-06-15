from django.contrib.auth.mixins import LoginRequiredMixin
from news_posts.models import NewsPosts
from django.contrib.auth import get_user_model
from django.views import generic
from communities.models import Communities



class UserDownVotedPostsView(LoginRequiredMixin, generic.DetailView):
    User = get_user_model()
    model = User
    template_name = 'users/down_voted_posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['down_voted_posts'] = NewsPosts.objects.filter(voted_user=self.kwargs['pk']).order_by("-created_at")
        context['communities_list'] = Communities.objects.filter(member=self.kwargs['pk']).order_by("-created_at")
        return context