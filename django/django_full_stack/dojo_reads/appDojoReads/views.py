from django.shortcuts import render, redirect
from .models import User, Book
from django.contrib import messages
import bcrypt
from django.db.models import Count
from datetime import datetime


def login_reg(request):
    return render(request, 'login_reg.html')

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
            request.session['user_id'] = user.id  # important!!!
    return redirect('/books')

def Login(request):
    if request.method == "POST":
        user_email = User.objects.filter(email=request.POST['email'])
        if user_email:
            user = user_email[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id  # important
                return redirect('/books')
            else:
                messages.error(request, "Incorrect email or password")
        else:
            messages.error(request, "Incorrect email or password")
    return redirect('/')


# def logout(request):
#     if 'logout' in request.POST:
#         del request.session['user_id'] # delete the session
#     return redirect('/')


def all_books(request):
    if 'user_id' not in request.session:  # makes sure user is in session to view content
        return redirect("/")
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'books': Book.objects.all()
    }
    return render(request, 'all_books.html', context)

def addBook(request):
    context = {
        'books' : Book.objects.all()
    }
    return render(request,'add_book.html', context)

def createBook(request):
    errors = Book.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/books/add')
    else:
        book = Book.objects.create(title= request.POST['title'], author= request.POST['author'], review= request.POST['review'], uploaded_by=User.objects.get(id=request.session['user_id']))
        # messages.success(request,"Book was successfully created")
        book.users_who_review.add(request.session['user_id'])
        return redirect (f'/books/{book.id}')


def newBook(request, id):
    context = {
    'book' : Book.objects.get(id=id)
    }
    return render(request, 'some_book.html', context)