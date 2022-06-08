from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView
from news_posts.models import NewsPosts, Vote
from users.forms import LoginForm, ProfileEditForm, UserForm
from django.contrib.auth import views
from django.contrib.auth import authenticate, login, get_user_model
from django.views import generic
from communities.models import Communities
from news_posts.models import Comment
from users.models import bookmarked_posts
# Create your views here.

User = get_user_model()

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = User.objects.create_user(username, email, password)
            user.save()
            auth_user = authenticate(request, username=username, password=password)
            login(request, auth_user)
            return HttpResponseRedirect(reverse('news_posts:index'))
    else:
        form = UserForm()

        remove_forms = ['password1', 'password2']

    return render(request, 'users/signup.html', {'form': form, 'remove_forms': remove_forms})

class LoginView(views.LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'


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

class ProfileEditView(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = ProfileEditForm
    template_name = 'users/profile_edit.html'
    def get_success_url(self):
        return reverse('users:detail', kwargs={'pk': self.request.user.id})

    def get_object(self):
        return self.request.user

class SavedPostDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'users/saved_post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['communities_list'] = Communities.objects.filter(member=self.kwargs['pk']).order_by("-created_at")
        context['saved_posts'] = NewsPosts.objects.filter(saved_user=self.kwargs['pk']).order_by("saved_at__created_at").reverse()
        return context

class UsersCommentsView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'users/comments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments_list'] = Comment.objects.filter(user=self.kwargs['pk']).order_by("-created_at")
        context['communities_list'] = Communities.objects.filter(member=self.kwargs['pk']).order_by("-created_at")
        return context

class UserUpVotedPostsView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'users/up_voted_posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['up_voted_posts'] = Vote.objects.filter(voted_user=self.kwargs['pk'], flag=1).order_by("-created_at")
        context['communities_list'] = Communities.objects.filter(member=self.kwargs['pk']).order_by("-created_at")
        return context

class UserDownVotedPostsView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'users/down_voted_posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['down_voted_posts'] = Vote.objects.filter(voted_user=self.kwargs['pk'], flag=-1).order_by("-created_at")
        context['communities_list'] = Communities.objects.filter(member=self.kwargs['pk']).order_by("-created_at")
        return context