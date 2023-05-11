from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from django.core.cache import cache
from .models import homepage
from datetime import datetime

# Create your views here.
class HomeView(View):
    def get(self, request):
        cache.clear()
        now = datetime.now()
        current_year = now.year
        homepage_model = homepage.objects.all()
        return render(request, 'ideapadapp1/homepage.html', {'homepage_model': homepage_model, 'current_year': current_year})

class AboutView(View):
    def get(self, request):
        cache.clear()
        return render(request, 'ideapadapp1/about.html')