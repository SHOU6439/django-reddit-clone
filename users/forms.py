from django import forms
from django.forms import fields, widgets
from users.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserForm(UserCreationForm):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)
    password1 = forms.CharField(required=False)
    password2 = password1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field, value in zip(self.fields, self.fields.values()):
            value.widget.attrs["class"] = 'input-userinfo-textarea'
            value.widget.attrs["placeholder"] = field.upper()
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
class LoginForm(AuthenticationForm):
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field, value in zip(self.fields, self.fields.values()):
            value.widget.attrs["class"] = 'input-userinfo-textarea'
            value.widget.attrs["placeholder"] = field.upper()
    class Meta:
        model = User
        fields = ('email', 'password')

class ProfileEditForm(forms.ModelForm):
    username = forms.CharField(max_length=20, widget=forms.widgets.TextInput(attrs={'class': "profile-edit-new-name-input-textarea", 'placeholder': "Display name(optional)"}))
    about = forms.CharField(max_length=200, widget=forms.widgets.Textarea(attrs={'class': "profile-edit-new-user-about-input-textarea", 'placeholder': "About(optional)"}), required=False)

    class Meta:
        model = User
        fields = ('username', 'about', 'photo', 'header_photo')
