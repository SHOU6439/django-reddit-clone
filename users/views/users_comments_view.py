from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views import generic
from django.db.models import Model
from users.usecases.users_comments_action import users_comments_action

class UsersCommentsView(LoginRequiredMixin, generic.DetailView):
    User: Model = get_user_model()
    model = User
    template_name: str = 'users/comments.html'

    def get_context_data(self, **kwargs: dict) -> dict:
        context = super().get_context_data(**kwargs)
        users_comments_action(context, self.kwargs['pk'])
        return context
