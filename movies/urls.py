# movies/urls.py
from django.urls import path

from . import views

# urlpatterns = [
#   path('answer', views.answer, name='answer'),
# ]

urlpatterns = [
    path('answer', views.choose_theater, name='choose-theater'),
    path('choose-movie', views.choose_movie, name='choose-movie'),  # <--- add this
    path('list-showtimes', views.list_showtimes, name='list-showtimes'),
]