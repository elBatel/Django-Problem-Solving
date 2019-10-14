""" series/urls.py """
from django.urls import path
from .views import SeriesDetailView, EpisodeDetailView, SeriesListView

app_name    = 'series'

urlpatterns = [
    path('', SeriesListView.as_view(), name='list'),
    path('<slug>', SeriesDetailView.as_view(), name='serie'),
    path('<series_slug>/<int:episode_number>', EpisodeDetailView.as_view(), name='episode'),
]
