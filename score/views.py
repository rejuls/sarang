from django.shortcuts import render
from .models import Match


# Create your views here.
def Match_list(request):
    try:
        match=Match.objects.order_by('-id')[:2][::-1]
        cm=match[0]
        nm=match[1]
    except:
        match = None
        cm=''
        nm=''
    return render(request, 'home.html', {'match':match,'cm':cm,'nm':nm})

def Results_list(request):
    try:
        match=Match.objects.order_by('-id')[2:]
        curr=match[0]
    except:
        match = None
        curr = ''
    return render(request, 'results.html', {'match':match,'curr':curr})
