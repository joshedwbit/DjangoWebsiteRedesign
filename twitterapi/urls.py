from django.urls import path
from . import views
from .views import RecentNewsView

urlpatterns = [
    path('', RecentNewsView.as_view(), name='recent-news'),
]