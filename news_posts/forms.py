from django import forms
from django.db.models import fields
from .models import NewsPosts

class CreatePostForm(forms.ModelForm):
    title = forms.CharField(max_length=300, widget=forms.widgets.TextInput(attrs={'class': "post-title-input-textarea", 'placeholder': "Title"}))
    content = forms.CharField(max_length=512, widget=forms.widgets.Textarea(attrs={'class': "post-content-input-textarea", 'placeholder': "Text(Optional)"}))

    class Meta:
        model = NewsPosts
        fields = ('title', 'content')