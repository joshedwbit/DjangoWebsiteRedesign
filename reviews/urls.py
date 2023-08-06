from django.urls import path
from . import views
from .views import leaveAReviewView

urlpatterns = [
    path('', leaveAReviewView.as_view(), name='leave-a-review'),
]
