from django.urls import path

from . import views

app_name = 'ftp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:filename>/download', views.download, name="download"),
    path('upload/', views.upload, name="upload"),
    path('fetchDir/', views.fetchDir, name="fetchDir")
]