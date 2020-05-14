from django.shortcuts import render, redirect
from .models import User, Book
from django.contrib import messages
import bcrypt
from django.db.models import Count
from datetime import datetime

# GET


def login_reg(request):
    return render(request, 'log_in.html')


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
    return redirect('/all_books')


def Login(request):
    if request.method == "POST":
        user_email = User.objects.filter(email=request.POST['email'])
        if user_email:
            user = user_email[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id  # important
                return redirect('/all_books')
            else:
                messages.error(request, "Incorrect email or password")
        else:
            messages.error(request, "Incorrect email or password")
    return redirect('/')


def all_books(request):
    if 'user_id' not in request.session:  # makes sure user is in session to view content
        return redirect("/")
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'books': Book.objects.all()
    }
    return render(request, 'all_books.html', context)


def logout(request):
    if 'logout' in request.POST:
        del request.session['user_id'] # delete the session
    return redirect('/')


def add_book(request):
    if request.method == "POST":
        errors = Book.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.errors(request, value)
        else:
            some_book = Book.objects.create(
                title=request.POST['title'],
                uploaded_by=User.objects.get(id=request.session['user_id']), desc=request.POST['desc'])
            some_book.users_who_like.add(request.session['user_id'])
    return redirect('/all_books')


def userBook(request, id):
    if request.method == 'GET':
        context = {
            'book': Book.objects.get(id=id),
            'user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, 'usersBook.html', context)


def addFavorite(request,id):
    if request.method == "POST":
        bookToFavorite = Book.objects.filter(id=id)
        if bookToFavorite:
            book = bookToFavorite[0]
            user = User.objects.get(id=request.session['user_id'])
            book.users_who_like.add(user)
    return redirect('/all_books')


def viewBook(request, id):
    context = {
        'book': Book.objects.get(id=id),
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'book.html', context)


def updateBook(request, id):
    if request.method == 'POST':
        bookToUpdate = Book.objects.filter(id=id) #added this line with daisy... asks if that book id is in the array
        if len(bookToUpdate) > 0: # added this line with daisy... if length of array 1 or greater..
            errors = Book.objects.basic_validator(request.POST) # then errors will pop up... must put in html.. that one piece of logic we always copy and paste
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.errors(request, value)
            else:
                book = Book.objects.get(id=id)
                book.title = request.POST['title']
                book.desc = request.POST['desc']
                book.save()
            return redirect('/all_books')
        else:
            messages.error(request, "Invalid ID")  # then post this message
            return redirect('/all_books')


def deleteBook(request, id):
    if request.method == 'POST':
        bookToDelete = Book.objects.filter(id=id)
        if bookToDelete:
            book = bookToDelete[0]
            user = User.objects.get(id=request.session['user_id'])
            if book.uploaded_by == user:
                book.delete()
    return redirect('/all_books')

def unFavorite(request,id):
    if request.method == "POST":
        bookToUnFavorite = Book.objects.filter(id=id)
        if bookToUnFavorite:
            book = bookToUnFavorite[0]
            user = User.objects.get(id=request.session['user_id'])
            book.users_who_like.remove(user)
    return redirect('/all_books')

def listOfBooks(request, id):
    if 'user_id' not in request.session:  # makes sure user is in session to view content
        return redirect("/")
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'books': Book.objects.all()
    }
    return render(request, 'users_favorite_books.html', context)









# def update(request):
#     if request.method == 'GET'
#     context = {
#             'book': Book.objects.get(id=id),
#             'user': User.objects.get(id=request.session['user_id'])
#         }
#     return redirect('/editBook')

#date/time validation
# x = requestPOST['created_at']
# y = datetime.strptime(x,'%Y-%m-%d').date()
# print(datetime.now().date())
# if y >= datetime.now().date():
#     errors['created_at'] = "date must be in past"