from django.views import View
from django.shortcuts import render
from django.core.cache import cache
from .forms import leaveAReviewForm
from .models import leaveAReviewText

class leaveAReviewView(View):
    def get(self, request):
        cache.clear()

        form = leaveAReviewForm()
        leaveAReviewText_model = leaveAReviewText.objects.first()
        return render(request, 'reviews/leaveareview.html',
        {
            'form': form,
            'introText': leaveAReviewText_model
        })

    def post(self, request):
        cache.clear()

        form = leaveAReviewForm(request.POST)
        if form.is_valid():
            form.save()
                # handle successful submission here
                # return redirect('success_url')
        return render(request, 'reviews/leaveareview.html',
        {
            'form': form
        })
