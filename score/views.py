from django.shortcuts import render
from .models import Match


# Create your views here.
def Match_list(request):
    match=Match.objects.order_by('-id')[:2][::-1]
    cm=match[0]
    nm=match[1]
    return render(request, 'home.html', {'match':match,'cm':cm,'nm':nm})

def Results_list(request):
    match=Match.objects.order_by('-id')[2:]
    curr=match[0]
    return render(request, 'results.html', {'match':match,'curr':curr})
