from django.forms import ModelForm
from .models import Question, Answer
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AskForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text', 'author']


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question', 'author']


class SignUpForm(ModelForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
