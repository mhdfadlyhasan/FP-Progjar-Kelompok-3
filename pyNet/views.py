from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from chat.models import Account
from .form_login import Login,SignUp




def signup(request):
    print(request.method)
    if request.method == 'POST':
        form = SignUp(request.POST)
        print(request)
        if form.is_valid():
            form.save()
            Acc_name = form.cleaned_data.get('user_name_chat')
            email = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = Account(Acc_name=Acc_name,Acc_email=email,Acc_password=raw_password)
            user.save()
            return redirect('home')
        else:
            print("form is not valid")
    else:
        form = SignUp()
    return render(request, './registration/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            print(email,raw_password)
            print(request)
            return redirect('home')
        else:
            print("form is not valid")
    else:
        form = Login()
    return render(request, './registration/login.html',{'form': form})