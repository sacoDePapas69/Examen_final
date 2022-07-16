from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from store.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']