from django.urls import path
from django.conf import settings

from .views import movie_list, movie_detail

app_name = 'cinema'

BASE_API_URL = settings.BASE_API_URL
urlpatterns = [
    path('movies/', movie_list, name='movie_list'),
    path('movies/<int:pk>', movie_detail, name='movie_list'),
]
