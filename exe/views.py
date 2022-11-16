from django.db.models import Model
from django.shortcuts import render
from.models import *


menu = ["About", "Clusters", "Write an Opus", "Feedback", "Login"]


def index(request):
    posts = Opus.objects.all()
    # clusters = Cluster.objects.all()
    context = {
        'posts': posts,
        # 'clusters': clusters,
        'menu': menu,
        'title': 'НиХеРаСебе!'
    }
    return render(request, 'exe/index.html', context=context)


def show_opus(request, opus_id):
    context = {

    }
    return render(request, 'exe/opus.html', context=context)    #diff templates for article / exercise


def about(request):
    return render(request, 'exe/about.html')


def show_cluster(request):
    pass

#
# class TaskView():
#     pass
