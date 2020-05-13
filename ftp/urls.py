from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:filename>/download', views.download, name="download"),
    path('upload', views.upload, name="upload")
]