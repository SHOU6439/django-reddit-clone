from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from users.forms import UserForm
from users.usecases.signup_action import signup_action

def signup(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            signup_action(request, form)
            return HttpResponseRedirect(reverse('news_posts:hot_index'))
    else:
        form = UserForm()

        remove_forms = ['password1', 'password2']

    return render(request, 'users/signup.html', {'form': form, 'remove_forms': remove_forms})