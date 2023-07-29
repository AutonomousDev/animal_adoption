from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    subscribe = forms.BooleanField(required=False, initial=True, widget=forms.CheckboxInput)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        # Create or update the Profile instance
        profile, created = Profile.objects.get_or_create(user=user)
        profile.subscribed = self.cleaned_data['subscribe']
        profile.save()

        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    subscribed = forms.BooleanField(required=False, initial=True, widget=forms.CheckboxInput)

    class Meta:
        model = Profile
        fields = ['subscribed']

        
