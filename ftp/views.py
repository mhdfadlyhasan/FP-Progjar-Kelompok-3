from django.shortcuts import render
from django.http import HttpResponse
from ftplib import FTP
from django.contrib.auth.decorators import login_required

f = FTP()


def login(request):
    f.connect('127.0.0.1', 8009)
    f.login('dex', '123')
    # if(request.method == 'POST'):
    pass


def logout():
    f.quit()


@login_required(login_url='/login/')
def index(request):
    return render(request, 'ftp/index.html')


def download(request, filename):
    return HttpResponse(filename)


def upload(request):
    return HttpResponse("Test")
