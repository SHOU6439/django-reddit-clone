from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.shortcuts import render, redirect
from django.views import generic
from django.utils import timezone
from communities.models import Communities
from news_posts.models import NewsPosts
from news_posts.forms import CreatePostForm



class CreatePostView(LoginRequiredMixin, generic.View):
    model = NewsPosts
    form_class = CreatePostForm
    template_name = 'news_posts/create_post.html'
    success_url = reverse_lazy('news_posts:index')

    def get(self, request, *args, **kwargs):
        # formにリクエストリクエストユーザー情報を渡す
        form = self.form_class(user=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CreatePostForm(user=request.user, data=request.POST)
        if form.is_valid():
            post_data = form.save(commit=False)
            post_data.user = get_user_model().objects.get(id=request.user.id)
            post_data.photo = request.FILES.get('photo')
            post_data.save()
            if post_data.community:
                post_community_at = Communities.objects.get(id=post_data.community.id)
                post_community_at.latest_posted_at = timezone.now()
                post_community_at.save()
            return redirect('news_posts:index')
        return redirect('news_posts:create_post')

    def get_queryset(self):
        return Communities.objects.all()