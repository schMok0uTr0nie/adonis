from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="homepage"),    # agora/   redirect
    path('post/<int:post_id>/', show_opus, name='opus'),   # exe vsv opus (diff structure)
    path('<cluster_slug>/', show_cluster, name='cluster')
    # path('<slug>/', taskView.as_view(), name="exercise"),
    # path('cats/<tag_slug>/', categories, name=""),  #slug arms
]