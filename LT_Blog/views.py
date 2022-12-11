from django.shortcuts import render
from django.http import Http404


def index(request):
    try:
        return render(request, 'index.html')
    except:
        raise Http404()