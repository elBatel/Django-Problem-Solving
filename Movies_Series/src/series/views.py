""" series/views.py """
from django.shortcuts import render
from django.views.generic import DetailView, View, ListView
from .models import Series, Episode

class SeriesListView(ListView):
    model = Series

class SeriesDetailView(DetailView):
    model   = Series

class EpisodeDetailView(View):

    def get(self, request, series_slug, episode_number, *args, **kwargs):
        serie_qs   = Series.objects.filter(slug=series_slug)
        if serie_qs.exists():
            serie  = serie_qs.first()

        episode_qs   = serie.episodes.filter(episode_number=episode_number)
        if episode_qs.exists():
            episode  = episode_qs.first()

        context = {'object': episode}
        return render(request, 'series/episode_detail.html', context)
