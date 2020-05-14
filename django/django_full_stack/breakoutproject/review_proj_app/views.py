from django.shortcuts import render, redirect
from .models import User, Cat
from django.contrib import messages
import bcrypt
from django.db.models import Count

def index(request):
    return render(request, "index.html")

def createUser(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            print("User's password entered was " + request.POST['password'])
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(name=request.POST['name'], password=hashed_pw)
            print("User's password has been changed to " + user.password)
            request.session['user_id'] = user.id
    return redirect('/homepage')

def login(request):
    if request.method == "POST":
        users_with_name = User.objects.filter(name=request.POST['name'])
        if users_with_name:
            user = users_with_name[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id #IMPORTANT!!!
                return redirect('/homepage')
            else:
                print("Password didn't match")
                messages.error(request, "Incorrect name or password")
        else:
            print("Name not found")
            messages.error(request, "Incorrect name or password")
    return redirect('/')

def homepage(request):
    context = {
        'user' : User.objects.get(id=request.session['user_id']),
        'cats' : Cat.objects.annotate(votes=Count('users_who_voted_for')).order_by('-votes')
    }
    return render(request,"main_page.html",context) #<--- And inside of here!

def createCat(request):
    #Logic to create a Cat, you should validate!
    if request.method == "POST":
        errors = Cat.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            some_cat = Cat.objects.create(
            cat_name = request.POST['cat_name'],
            owner = User.objects.get(id=request.session['user_id'])
        )
    return redirect('/homepage')

def deleteCat(request, id):
    if request.method == "POST":
        catToDelete = Cat.objects.filter(id=id)
        if catToDelete:
            cat = catToDelete[0]    #handles deleting cat id
            user = User.objects.get(id=request.session['user_id'])
            if cat.owner == user:
                cat.delete()
    return redirect('/homepage')

def VoteCat(request, id):
    if request.method == "POST":
        catToVote = Cat.objects.filter(id=id)
        if catToVote:
            cat = catToVote[0] 
            user = User.objects.get(id=request.session['user_id'])
            cat.users_who_voted_for.add(user)
    return redirect('/homepage')

def unVoteCat(request, id):
    if request.method == "POST":
        
        catToVote = Cat.objects.filter(id=id)
        if catToVote:
            cat = catToVote[0]    #handles deleting cat id
            user = User.objects.get(id=request.session['user_id'])
            cat.users_who_voted_for.remove(user)
    return redirect('/homepage')

def userProfile(request):
    context = {
        "user" : User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'one_user.html', context)

def catProfile(request, id):
    catToVote = Cat.objects.filter(id=id)
    if catToVote:
        cat = catToVote[0]
        context = {
            "cat": cat
        }
        return render(request, "one_cat.html", context)
    else:
        return redirect('/homepage')