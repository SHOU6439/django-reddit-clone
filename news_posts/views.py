from sys import flags
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views import generic
from communities.models import Communities
from users.models import User
from .models import NewsPosts, Comment, Vote
from .forms import CreateCommentForm, CreatePostForm, NewsPostEditForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
# Create your views here.

class IndexView(generic.ListView):
    model = NewsPosts
    template_name = 'news_posts/index.html'

    def get_context_data(self, **kwargs):
        # post = NewsPosts.objects.get(pk=self.kwargs.pk)
        print(self.kwargs)
        context = super().get_context_data(**kwargs)
        context['post_list'] = NewsPosts.objects.order_by('-created_at')
        context['vote_list'] = Vote.objects.filter(voted_user_id=self.request.user.id)
        context['communities_list'] = Communities.objects.order_by('-created_at')
        return context

class CreatePostView(LoginRequiredMixin, generic.CreateView):
    model = NewsPosts
    form_class = CreatePostForm
    template_name = 'news_posts/create_post.html'
    success_url = reverse_lazy('news_posts:index')
    def post(self, request):
        form = CreatePostForm(request.POST)

        post_data = form.save(commit=False)
        post_data.user = get_user_model().objects.get(id=request.user.id)
        post_data.photo = request.FILES.get('photo')
        post_data.save()
        return redirect('news_posts:index')

    def get_queryset(self):
        return Communities.objects.all()


class DeletePostView(LoginRequiredMixin, generic.DeleteView):
    model = NewsPosts
    success_url = reverse_lazy('news_posts:index')

class DeleteLoginUserPostView(LoginRequiredMixin, generic.DeleteView):
    model = NewsPosts
    def get_success_url(self):
        return reverse('users:detail', kwargs={'pk': self.request.user.id})

class DeleteCommentView(LoginRequiredMixin, generic.DeleteView):
    model = Comment
    success_url = reverse_lazy('news_posts:index')

class NewsPostDetailView(LoginRequiredMixin, generic.DetailView):
    model = NewsPosts
    template_name = 'news_posts/post_detail.html'
    def get_context_data(self, **kwargs):
        post_pk = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['comment_list'] = Comment.objects.filter(target=post_pk)
        return context
class NewsPostEditView(LoginRequiredMixin, generic.UpdateView):
    model = NewsPosts
    form_class = NewsPostEditForm
    template_name = 'news_posts/post_edit.html'
    def get_success_url(self):
        post_pk = self.kwargs['pk']
        return reverse('news_posts:post_detail', kwargs={'pk': post_pk})
class CreateCommentView(LoginRequiredMixin, generic.CreateView):
    template_name = 'news_posts/create_comment.html'
    form_class = CreateCommentForm
    model = Comment

    # def post(self, request):
    #     form = CreateCommentForm(request.POST)

    #     get_user_id = form.save(commit=False)
    #     get_user_id.user = get_user_model().objects.get(id=request.user.id)
    #     get_user_id.save()
    #     return redirect('news_posts:index')

    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(NewsPosts, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post
        comment.user = get_user_model().objects.get(id=self.request.user.id)
        comment.save()
        return redirect('news_posts:post_detail', pk=post_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['target_post'] = get_object_or_404(NewsPosts, pk=self.kwargs['pk'])
        return context

@login_required
@transaction.atomic
def vote_up(request, pk):
    # print('up')
    post = NewsPosts.objects.get(pk=pk)
    vote = Vote.objects.filter(voted_user=request.user, voted_post=post).first()
    if not vote:
        vote = Vote()
        # print('up, none')
        vote.voted_user = request.user
        vote.voted_post = post
        vote.flag = 0
    if vote.flag <= 0:
        # print('up, -1 or 0')
        vote.flag += 1
        post.vote += 1
    else:
        # print('up, 1')
        vote.flag -= 1
        post.vote -= 1
    vote.save()
    post.save()
    return redirect('news_posts:index')

@login_required
@transaction.atomic
def vote_down(request, pk):
    # print('down')
    post = NewsPosts.objects.get(pk=pk)
    vote = Vote.objects.filter(voted_user=request.user, voted_post=post).first()
    if not vote:
        # print('down, none')
        vote = Vote()
        vote.voted_user = request.user
        vote.voted_post = post
        vote.flag = 0
    if vote.flag >= 0:
        # print('down, 0 or 1')
        vote.flag -= 1
        post.vote -= 1
    else:
        # print('down, -1')
        vote.flag += 1
        post.vote += 1
    vote.save()
    post.save()
    return redirect('news_posts:index')

# class CreateReplayView(LoginRequiredMixin, generic.CreateView):
#     model = Replay
#     form_class = CreateReplayForm
#     template_name = "news_posts/create_replay.html"

#     def form_valid(self, form):
#         comment_pk = self.kwargs['pk']
#         comment = get_object_or_404(Comment, pk=comment_pk)
#         replay = form.save(commit=False)
#         replay.target = comment
#         replay.user = get_user_model().objects.get(id=self.request.user.id)
#         replay.save()
#         return redirect('news_posts:post_detail', pk=comment_pk)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['target_comment'] = get_object_or_404(Comment, pk=self.kwargs['pk'])
#         return context
