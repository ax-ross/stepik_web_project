from django.forms import ModelForm
from .models import Question
from django import forms


class AskForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text']

    #def clean_text(self):
        #text = self.cleaned_data['text']
        #if not text.is_valid():
            #raise forms.ValidationError('question text is wrong')
        #return text

    #def clean_title(self):
        #title = self.cleaned_data['title']
        #if not title.is_valid():
            #raise forms.ValidationError('title text is wrong')
        #return title

