from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .form_login import SignUp, Login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

@login_required(login_url='/login/')
def home(request):
    print("User is logged in!")
    return redirect('home')


def signup(request):
    print(request.method)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(request)
        if form.is_valid():
            raw_password = form.cleaned_data.get('password1')
            User_name = form.cleaned_data.get('username')
            user = form.save()
            user.is_active = False
            user.save()
            login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        else:
            print("form is not valid")
    else:
        form = UserCreationForm()
    return render(request, './registration/register.html', {'form': form})

def logins(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=raw_password, is_active = True)
            if user:
                print (user.is_active)
                login(request, user)
                return redirect('home')
            else: 
                print("User is not found" )
                return redirect('Login')
        else:
            print("form is not valid")
    else:
        form = Login()
    return render(request, './registration/login.html',{'form': form})