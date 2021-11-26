from django import forms
from django.db.models import fields
from django.db.models.fields import BLANK_CHOICE_DASH
from communities.models import Communities


class CommunityForm(forms.ModelForm):
    name = forms.CharField(max_length=21, widget=forms.widgets.TextInput(attrs={'class': "community-name-input-textarea"}))
    community_type = forms.fields.ChoiceField(
        choices = (
            ('0','public'),
            ('1','restrict'),
            ('2','private'),
        ),
        required=True,
        widget=forms.widgets.RadioSelect(attrs={'class': "community-type-select-radio-button"}),
    )
    is_nsfw = forms.BooleanField(
        widget=forms.widgets.CheckboxInput(attrs={'class':"community-is-nsfw-check"}),
        required=False
    )

    class Meta:
        model = Communities
        fields = ('name', 'community_type', 'is_nsfw')