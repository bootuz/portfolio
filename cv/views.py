from django.shortcuts import render

# Create your views here.
from cv.models import Profile


def index(request):
    profile = Profile.objects.get(name__contains='Astemir Boziev')

    context = {
        'profile': profile
    }
    return render(request, 'cv/index.html', context=context)




