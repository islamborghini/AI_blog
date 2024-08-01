from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta: 
        #whenever form validates we wanna create a user
        model = User

        #fields to show in the form
        fields = ['username', 'email', 'password1', 'password2']
