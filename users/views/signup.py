from django.shortcuts import render
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from users.forms import UserForm
from django.contrib.auth import authenticate, login, get_user_model

def signup(request):
    User = get_user_model()
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
            return HttpResponseRedirect(reverse('news_posts:hot_index'))
    else:
        form = UserForm()

        remove_forms = ['password1', 'password2']

    return render(request, 'users/signup.html', {'form': form, 'remove_forms': remove_forms})