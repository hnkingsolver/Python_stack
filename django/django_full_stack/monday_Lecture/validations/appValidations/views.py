from django.shortcuts import render, HttpResponse, redirect
from .models import Phillip
from django.contrib import messages


def index(request):
    context = {
        "phillips": Phillip.objects.all() 
    }
    return render(request, 'index.html', context)

def create(request):
    errors = Phillip.objects.create_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/') #go back the place of the form
    else:
        Phillip.objects.create(name=request.POST['name'], model_no=request.POST['model_no'], email=request.POST['email'])
        return redirect('/') #go to next part of application