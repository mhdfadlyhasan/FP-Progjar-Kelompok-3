from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .form_login import SignUp, Login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

# Encode and decode userId for validation process
# https://www.youtube.com/watch?v=zG7DZqDwYq0
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site

token = PasswordResetTokenGenerator()

@login_required(login_url='/login/')
def home(request):
    print("User is logged in!")
    return redirect('home')

def signup(request):
    print(request.method)
    if request.method == 'POST':
        form = SignUp(request.POST)
        print(request)
        if form.is_valid():
            raw_password = form.cleaned_data.get('password1')
            User_name = form.cleaned_data.get('username')
            user = form.save()
            user.is_active = False
            user.save()
            # login(request, user,backend='django.contrib.auth.backends.ModelBackend')

            # Build and send email to current user
            verificationEmail = EmailMessage(
                "Verify that this is you",
                # Message based on template
                render_to_string('registration/verify.html',
                {
                    'user': user,
                    'domain': get_current_site(request),
                    'uId': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': token.make_token(user)
                }),
                settings.EMAIL_HOST_USER,
                [user.email]
            )
            verificationEmail.send()
            return redirect('home')
        else:
            print("form is not valid")
    else:
        form = SignUp()
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

def activate(request, uidb64, linkToken):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception as identifier:
        user = None
    
    if user is not None and token.check_token(user, linkToken):
        user.is_active = True
        user.save()
        return redirect('home')
    return "<h3>Something is wrong</h3>"

def logout_(request):
    logout(request)
    return redirect('login')