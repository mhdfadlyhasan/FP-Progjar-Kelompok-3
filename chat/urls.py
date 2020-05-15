from django.urls import path

from . import views

app_name = 'ftp'
urlpatterns = [
    path('', views.index, name='index'),
]