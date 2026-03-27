from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","password1", "password2")


class LoginForm(AuthenticationForm):
    key_file = forms.FileField(required=True, label="Private Key File (.pem)")
