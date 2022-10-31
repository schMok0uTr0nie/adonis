from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="homepage"),    # agora/   redirect
    # path('<slug>/', taskView.as_view(), name="exercise"),
    # path('cats/<tag_slug>/', categories, name=""),  #slug arms
]