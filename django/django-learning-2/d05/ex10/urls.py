from django.urls import path
from . import views

urlpatterns = [
    path('', views.character_search, name='character_search'),
]