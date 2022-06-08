from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from communities.models import Communities
from news_posts.models import NewsPosts
from users.models import User

class ProfileDetailView(LoginRequiredMixin ,generic.DetailView):
    model = User
    template_name = 'users/profile_detail.html'
    # def get(self, request, *args, **kwargs):
    #     user_data = User.objects.get(id=request.user.id)

    #     return render(request, 'users/profile_detail.html', {
    #         'user_data': user_data,
    #     })
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userpost_list'] = NewsPosts.objects.filter(user_id=self.kwargs['pk']).order_by("-created_at")
        context['communities_list'] = Communities.objects.filter(member=self.kwargs['pk']).order_by("-created_at")
        context['saved_posts'] = NewsPosts.objects.filter(saved_user=self.request.user.id)
        return context