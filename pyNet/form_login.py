from django import forms
from django.contrib.auth.forms import UserCreationForm

class Login(forms.Form):
    email = forms.CharField(label='Name', max_length=100)
    password = forms.CharField(label='password', max_length=100)

class SignUp (UserCreationForm):#exteding UserCreation, adding UsernameChat!
    user_name_chat = forms.CharField(max_length=30, required=True)