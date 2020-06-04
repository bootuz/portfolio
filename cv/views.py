from django.shortcuts import render

# Create your views here.
from cv.models import CV


def index(request):
    resume = CV.objects.filter(name='Astemir Boziev').first()

    context = {
        'resume': resume
    }
    return render(request, 'cv/index.html', context=context)


def resumes(request):
    return render(request, 'cv/resumes.html')




