from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from django.core.cache import cache

# Create your views here.
class HomeView(View):
    def get(self, request):
        cache.clear()
        return render(request, 'ideapadapp1/homepage.html')

class AboutView(View):
    def get(self, request):
        cache.clear()
        return render(request, 'ideapadapp1/about.html')