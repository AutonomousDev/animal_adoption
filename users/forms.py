from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    subscribe = forms.BooleanField(required=False, initial=True, widget=forms.CheckboxInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'subscribe']
