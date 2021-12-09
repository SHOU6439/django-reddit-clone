from django import forms
from django.db.models import fields
from .models import NewsPosts
from communities.models import Communities


class CreatePostForm(forms.ModelForm):
    CHOICES = Communities.objects.all()
    title = forms.CharField(max_length=300, widget=forms.widgets.TextInput(attrs={'class': "post-title-input-textarea", 'placeholder': "Title"}))
    content = forms.CharField(max_length=512, widget=forms.widgets.Textarea(attrs={'class': "post-content-input-textarea", 'placeholder': "Text(Optional)"}))
    # community = forms.ChoiceField(widget=forms.widgets.Select(attrs={'class': "post-select-community-field"}, choices=CHOICES))

    class Meta:
        model = NewsPosts
        fields = ('title', 'content' , 'photo', 'community')