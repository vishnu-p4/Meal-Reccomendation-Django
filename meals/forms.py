from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": " username form-control", "placeholder": "Username"}
        ),
    )
    password1 = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": " password form-control", "placeholder": "Password"}
        ),
    )
    password2 = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": " password form-control", "placeholder": "Re-enter Password"}
        ),
    )

    

    class Meta:
        model = User
        fields = (
            "username",
            "password1",
            "password2",

        )

