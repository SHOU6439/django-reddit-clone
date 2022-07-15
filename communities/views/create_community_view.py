from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls.base import reverse_lazy
from django.views import generic
from communities.forms import CommunityForm
from communities.models import Communities
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.db.models import Model
from django.forms import ModelForm

class CreateCommunityView(LoginRequiredMixin, generic.CreateView):
    template_name: str = 'communities/create_community.html'
    model: Model = Communities
    form_class: ModelForm = CommunityForm
    success_url = reverse_lazy('news_posts:hot_index')

    def post(self, request: HttpRequest) -> HttpResponseRedirect:
        form = CommunityForm(request.POST)

        post_data = form.save(commit=False)
        post_data.admin = get_user_model().objects.get(id=request.user.id)
        post_data.save()
        community = Communities.objects.get(name=post_data.name)
        # adminがコミュニティを作ったら自動的にadminはmemberに追加する
        community.member.add(request.user.id)
        community.save()
        return redirect('communities:detail', pk=community.id)