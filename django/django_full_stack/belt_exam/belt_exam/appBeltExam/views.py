from django.shortcuts import render, redirect
from .models import User, Quote
from django.contrib import messages
import bcrypt
from django.db.models import Count

def index(request):
    return render(request, "login.html")

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
    return redirect('/homepage')


def login(request):
    if request.method == "POST":
        user_email = User.objects.filter(email=request.POST['email'])
        if user_email:
            user = user_email[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id  # important
                return redirect('/homepage')
            else:
                messages.error(request, "Incorrect email or password")
        else:
            messages.error(request, "Incorrect email or password")
    return redirect('/')

def logout(request):
    if request.method == "POST":
        del request.session['user_id'] # delete the session
    return redirect('/')

def homepage(request):
    if 'user_id' not in request.session:  # makes sure user is in session to view content
        return redirect("/")
    context = {
        'user' : User.objects.get(id=request.session['user_id']),
        'quotes' : Quote.objects.all()
    }
    return render(request,"homepage.html",context) 

def post_quote(request):
    if request.method == "POST":
        errors = Quote.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            some_quote = Quote.objects.create(
                author=request.POST['author'],
                posted_by=User.objects.get(id=request.session['user_id']), quote=request.POST['quote'])
            some_quote.users_who_liked.add(request.session['user_id'])
    return redirect ('/homepage')

def userPage(request, id):
    if 'user_id' not in request.session:  # makes sure user is in session to view content
        return redirect("/")
    context = {
        'user' : User.objects.get(id=id),
        # 'quotes': Quote.objects.all
    }
    return render(request,"userspage.html",context)

def deleteQuote(request, id):
    if request.method == "POST":
        quoteToDelete = Quote.objects.filter(id=id)
        if quoteToDelete:
            quote = quoteToDelete[0]    #handles deleting quote id
            user = User.objects.get(id=request.session['user_id'])
            if quote.posted_by == user:
                quote.delete()
    return redirect('/post_quote')

def likeQuote(request, id):
    if request.method == "POST":
        quoteToLike = Quote.objects.filter(id=id)
        if quoteToLike:
            cat = quoteToLike[0] 
            user = User.objects.get(id=request.session['user_id'])
            cat.users_who_liked.add(user)
    return redirect('/post_quote')

def unLikeQuote(request, id):
    if request.method == "POST":
        
        quoteToLike = Quote.objects.filter(id=id)
        if quoteToLike:
            cat = quoteToLike[0]   
            user = User.objects.get(id=request.session['user_id'])
            cat.users_who_liked.remove(user)
    return redirect('/post_quote')

def editAccount(request, id):
    if 'user_id' in request.session:
        context = {
        'user' : User.objects.get(id=request.session['user_id'])
    }
    return render(request,'editaccount.html', context)

def updateAccount(request, id):
    if request.method == "POST":
        accountToUpdate = User.objects.filter(id=id)
        if len(accountToUpdate) > 0:
            errors = User.objects.update_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/editaccount/{id}')
        else:
            user = User.objects.get(id=id) #had to make another validator function in the User.Manager to update
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
        return redirect('/homepage')
    else:
        messages.error(request,"Invalid ID")
        return redirect('homepage')