from django.shortcuts import redirect
from django.urls.base import reverse_lazy
from django.views import generic
from communities.forms import CommunityForm
from communities.models import Communities
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

class CreateCommunityView(LoginRequiredMixin, generic.CreateView):
    template_name = 'communities/create_community.html'
    model = Communities
    form_class = CommunityForm
    success_url = reverse_lazy('news_posts:hot_index')
    def post(self, request):
        form = CommunityForm(request.POST)

        post_data = form.save(commit=False)
        post_data.admin = get_user_model().objects.get(id=request.user.id)
        post_data.save()
        community = Communities.objects.get(name=post_data.name)
        # adminがコミュニティを作ったら自動的にadminはmemberに追加する
        community.member.add(request.user.id)
        community.save()
        return redirect('communities:detail', pk=community.id)