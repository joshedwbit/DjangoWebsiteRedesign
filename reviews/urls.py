from django.urls import path
from . import views
from .views import LeaveAReviewView

urlpatterns = [
    path('', LeaveAReviewView.as_view(), name='leave-a-review'),
]
