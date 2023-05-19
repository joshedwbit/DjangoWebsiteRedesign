from django.urls import path
from . import views
from .views import LeaveAReveiwView

urlpatterns = [
    path('', LeaveAReveiwView.as_view(), name='leave-a-review'),
]
