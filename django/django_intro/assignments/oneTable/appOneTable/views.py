from django.shortcuts import render, HttpResponse, redirect
from.models import Dungeon
from.models import Prisoner


def root(request):
    # for i in Dungeon.objects.all():
        # ids=[]
        # names=[]
        # prisoners=[]
        # locations=[]
        # ids.append(i.id)
        # names.append(i.name)
        # prisoners.append(i.prisoners)
        # locations.append(i.locations)

    myvars = {
        # "id" : ids,
        # "name": names,
        # "prisoners": prisoners,
        # "location": locations,
        "db": Dungeon.objects.all(),
        "pr":Prisoner.objects.all()
    }

    return render(request, 'index.html', myvars)


def add(request):
    Dungeon.objects.create(name=request.POST['name'], num_people_inside=int(
        request.POST['prisoners']), location=request.POST['location'])
    return redirect('/')
# Create your views here.

def list(request):
    myvars ={
        "db": Dungeon.objects.all(),
        "pr":Prisoner.objects.all()
    }
    return render(request, 'list.html', myvars)

def addPrisoner(request):
    Prisoner.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], 
    dungeon=Dungeon.objects.get(id=request.POST['dungeon']))
    return redirect('/list')

def delete(request, id):
    Dungeon_to_delete = Dungeon.objects.get(id=id)
    Dungeon_to_delete.delete()
    return redirect('/list')