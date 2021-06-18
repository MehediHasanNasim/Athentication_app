from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProfilePicture
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = ProfilePicture
        fields = ['image']