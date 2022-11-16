from django import template
from exe.models import *

register = template.Library()

@register.simple_tag(name='getclusters')
def get_clusters(filter=None):
    if not filter:
        return Cluster.objects.all()
    else:
        return Cluster.objects.filter(pk=filter)


@register.inclusion_tag('exe/list_clusters.html')
def show_clusters(sort=None, cat_selected=0):
    if not sort:
        clusters = Cluster.objects.all()
    else:
        clusters = Cluster.objects.order_by(sort)

    return {"clusters": clusters, "cat_selected": cat_selected}