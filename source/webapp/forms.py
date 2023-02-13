from django import forms

from webapp.models import Phrase


class PhraseForm(forms.ModelForm):
    class Meta:
        model = Phrase
        fields = ['text', 'author', 'email']
