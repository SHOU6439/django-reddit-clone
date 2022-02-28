from django import forms

from chat.models import DirectMessage


class CreateDirectMessageForm(forms.ModelForm):
    content = forms.CharField(max_length=512, widget=forms.widgets.TextInput(attrs={'class': "dm-send-message-text-input", 'placeholder': "Message"}))

    class Meta:
        model = DirectMessage
        fields = ('content',)
