from django.shortcuts import render
from time import gmtime, strftime
from django.utils import timezone

def index(request):
    context = {
        "now" : timezone.now()
    }
    return render(request,'index.html', context)