from django.contrib import admin
from .models import *


# 10.11.22 =

class OpusAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'encode', 'cluster', 'rating', 'created', 'modified', 'is_published')
    # all except? / cluster_id?  / no tag (+) its ManyToMany /
    list_display_links = ('id', 'title', 'cluster')         # id? title?
    search_fields = ('author', 'title', 'encode', 'cluster')  # search
    list_editable = ('is_published',)    # encode?
    list_filter = ('cluster', 'is_published', 'created')   # filter
    prepopulated_fields = {"slug": ("title",)}       # slug made of title automatically


class ClusterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')
    list_display_links = ('id', 'value')
    search_fields = ('value',)       # comma for Tuple
    prepopulated_fields = {"slug": ("value",)}


admin.site.register(Opus, OpusAdmin)
admin.site.register(Cluster, ClusterAdmin)
admin.site.register(Tag, TagAdmin)