from django import forms
from django.contrib.auth.forms import UserCreationForm

class Login(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(),label='password', max_length=100)

class SignUp (UserCreationForm):#exteding UserCreation, adding UsernameChat!
    email = forms.EmailField(max_length=254, required = True)
    first_name = forms.CharField(max_length=30, required = True)
    last_name = forms.CharField(max_length=150, required = True)