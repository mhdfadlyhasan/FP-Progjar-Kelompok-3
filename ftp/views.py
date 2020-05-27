from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Code.pynetFTP.client import FTPClientModel
from django.contrib.auth.decorators import login_required
from pathlib import Path
import os


@login_required(login_url='/login/')
def index(request):
    if not FTPClientModel.isConnected:
        client = FTPClientModel().connect()

    dirs = client.list_dir('.')

    filenames = []
    attrs = []
    for file in dirs:
        if file[1]['type'] == 'file':
            filenames.append(file[0])
        attrs.append(file[1])

    context = {'attrs': attrs, 'filenames': filenames}
    return render(request, 'ftp/index.html', context=context)


def fetchDir(request):
    if not FTPClientModel.isConnected:
        client = FTPClientModel().connect()

    list_dirs = client.list_dir('.')
    dirs = []

    context = {'dirs': dirs}
    return JsonResponse(context)


def download(request, filename):
    fullpath = os.path.join(os.path.abspath('static/files'), filename)
    print(fullpath)

    if Path(fullpath).exists() and Path(fullpath).is_file():
        with open(fullpath, 'rb') as file:
            response = HttpResponse(file.read(),
                                    content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(fullpath)
        print(response)
        return response

    return HttpResponse(f"File {filename} doesnt exist")


def upload(request):
    return HttpResponse("Test")
