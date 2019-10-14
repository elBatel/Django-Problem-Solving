""" series/models.py  1 """
from django.db import models
from django.urls import reverse

class Series(models.Model):
    title       = models.CharField(max_length=120)
    slug        = models.SlugField()
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('series:serie', kwargs={'slug': self.slug})

    @property
    def episodes(self):
        return self.episode_set.all().order_by('episode_number')

""" series/models.py  2 """
class Episode(models.Model):
    title           = models.CharField(max_length=120)
    slug            = models.SlugField()
    series          = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True)
    episode_number  = models.IntegerField()
    episode_url     = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('series:episode', kwargs={'series_slug': self.series.slug, 'episode_number': self.episode_number})
