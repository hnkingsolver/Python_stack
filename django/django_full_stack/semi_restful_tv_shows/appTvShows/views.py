from django.shortcuts import render, HttpResponse, redirect
from .models import Show
from datetime import datetime, time, timezone
from time import gmtime, strftime
from django.contrib import messages

def index(request):
    return redirect('/shows')

def Allshows(request): #GET /shows
    context = {
        'shows' : Show.objects.all()
    }
    return render(request, 'all_shows.html', context)

def Addshow(request):
    context = {
        'shows' : Show.objects.all()
    }
    return render(request,'new_shows.html', context)

def createShow(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/shows/add') #go back the place of the form
    else:
        show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], desc=request.POST['desc'])
        messages.success(request, "Show successfully created")
        return redirect(f'/shows/{show.id}')

def tvShow(request, id): #GET /shows/<id>
    context = {
        'show' : Show.objects.get(id=id)
    }
    return render(request, 'tv_show.html', context)

def editShow(request, id):
    context = {
        'show' : Show.objects.get(id=id)
    }
    return render(request,'editShow.html', context)

def updateShow(request,id):
    print("Request", request)
    print(request.POST)
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{id}/edit')
    else:
        show = Show.objects.get(id=id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.desc = request.POST['desc']
        show.save()
    return redirect(f'/shows/{id}')

def DeleteShow(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')