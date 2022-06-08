from users.forms import LoginForm
from django.contrib.auth import views


class LoginView(views.LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'