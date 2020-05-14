from django.shortcuts import render, redirect
from .models import User, Group
from django.contrib import messages
import bcrypt
from django.db.models import Count

def index(request):
    return render(request, "log_in.html")

def register(request):
    print(request.POST)
    if request.method == "POST":
        errors = User.objects.create_validator(request.POST)
        if len(errors) > 0:
            print("Errors", errors)
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            pwhash = bcrypt.hashpw(
                request.POST['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(
                first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pwhash.decode())
            print("User: ", user)
            request.session['user_id'] = user.id  # important!!! session method that allows us to Set the value that will be stored by 'key' to 'value'
    return redirect('/groups')


def login(request):
    if request.method == "POST":
        user_email = User.objects.filter(email=request.POST['email'])
        if user_email:
            user = user_email[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id  # important
                return redirect('/groups')
            else:
                messages.error(request, "Incorrect email or password")
        else:
            messages.error(request, "Incorrect email or password")
    return redirect('/')

def logout(request):
    if request.method == "POST":
        del request.session['user_id'] # delete the session
    return redirect('/')

def groups(request):
    if 'user_id' not in request.session:  # makes sure user is in session to view content
        return redirect("/")
    context = {
        'user' : User.objects.get(id=request.session['user_id']),
        'groups' : Group.objects.all()
    }
    return render(request,"groups_all.html",context) 

def post_group(request):
    if request.method == "POST":
        errors = Group.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            some_group = Group.objects.create(
                name=request.POST['name'],
                desc=request.POST['desc'],
                added_by=User.objects.get(id=request.session['user_id']))
            some_group.members.add(request.session['user_id'])
    return redirect ('/groups')

def viewGroup(request, id):
    if 'user_id' not in request.session:  # makes sure user is in session to view content
        return redirect("/")
    context = {
        'group' : Group.objects.get(id=id),
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request,"group_page.html",context)

def joinGroup(request, id):
    if request.method == "POST":
        groupToJoin = Group.objects.filter(id=id)
        if groupToJoin:
            group = groupToJoin[0] 
            user = User.objects.get(id=request.session['user_id'])
            group.members.add(user)
    return redirect(f'/groups/{id}')

def unJoinGroup(request, id):
    if request.method == "POST":
        groupToUnJoin = Group.objects.filter(id=id)
        if groupToUnJoin:
            group = groupToUnJoin[0] 
            user = User.objects.get(id=request.session['user_id'])
            group.members.remove(user)
    return redirect(f'/groups/{id}')

def deleteGroup(request, id):
    if request.method == "POST":
        groupToDelete = Group.objects.filter(id=id)
        if groupToDelete:
            quote = groupToDelete[0]    #handles deleting quote id
            user = User.objects.get(id=request.session['user_id'])
            if quote.added_by == user:
                quote.delete()
    return redirect('/groups')