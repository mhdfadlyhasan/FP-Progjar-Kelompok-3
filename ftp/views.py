from django.shortcuts import render
from django.http import HttpResponse
from Code.pynetFTP.client import ClientFtp
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def index(request):
    global client
    if not ClientFtp.isConnect:
        client = ClientFtp().connect()

    paths = client.listdir('.')['paths']
    filenames = client.listdir('.')['filenames']

    context = {'paths': paths, 'filenames': filenames}
    return render(request, 'ftp/index.html', context=context)


def download(request, filename):
    return HttpResponse(filename)


def upload(request):
    return HttpResponse("Test")
