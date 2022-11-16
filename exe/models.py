from django.conf import settings
from django.db import models
from django.urls import reverse


# 31/10/22: Opus & Cluster |  08/11/22 added Tag  |

class Opus(models.Model):   # Post / Article / Tablet / Parchment
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)    # verif

    title = models.TextField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")
    encode = models.CharField(max_length=10)      # schema

    cluster = models.ForeignKey('Cluster', on_delete=models.PROTECT, null=True)   # + blank?
    tags = models.ManyToManyField('Tag', blank=True)   #make choice

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
        verbose_name = 'Opus'
        verbose_name_plural = 'Opuses'
        ordering = ['-created', 'title']   # title?


class Cluster(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cluster', kwargs={'cluster_slug': self.slug})

    class Meta:
        verbose_name = 'Cluster'
        verbose_name_plural = 'Clusters'
        ordering = ['name']      # id


class Tag(models.Model):
    value = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['value']