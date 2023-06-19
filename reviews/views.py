from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from django.core.cache import cache
from .forms import MyForm

class LeaveAReviewView(View):
    def get(self, request):
        cache.clear()
        return render(request, 'reviews/leaveareview.html')
