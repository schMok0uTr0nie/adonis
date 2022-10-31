from django.conf import settings
from django.db import models
from django.urls import reverse


# 31/10/22: Opus & Cluster |

class Opus(models.Model):   # Post / Article / Tablet / Parchment
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)    # verif

    title = models.TextField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    encode = models.CharField(max_length=10)      # schema

    clusters = models.ManyToManyField('Cluster', null=True, related_name="posts")
    content = models.TextField(blank=True)
    rating = models.IntegerField(null=True, blank=True)  #max = 100

    # videotutor = link  or preview?
    muscles = models.ImageField(upload_to="photos/anatomy/<encode>", blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('opus', kwargs={'opus_slug': self.slug})

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-created', 'title']   # title?


class Cluster(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cluster', kwargs={'cluster_slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']
