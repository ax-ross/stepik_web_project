from django.forms import ModelForm
from .models import Question, Answer
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AskForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text']


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
