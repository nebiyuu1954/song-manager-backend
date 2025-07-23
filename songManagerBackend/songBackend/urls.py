# songBackend/urls.py
from django.urls import path
from .views import SongDetailView,SongListView
from . import views

urlpatterns = [
    path('songs/', views.SongListView.as_view()),
    path('songs/<int:pk>/', views.SongDetailView.as_view()),
]