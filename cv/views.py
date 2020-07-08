from django.shortcuts import render, get_object_or_404

# Create your views here.
from cv.models import Profile


def index(request):
    profile = get_object_or_404(Profile, name='Astemir Boziev')

    context = {
        'profile': profile
    }
    return render(request, 'cv/index.html', context=context)




