from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def index(request):
    return HttpResponse("Hello dex")


def download(request, filename):
    return HttpResponse(filename)


def upload(request):
    pass
