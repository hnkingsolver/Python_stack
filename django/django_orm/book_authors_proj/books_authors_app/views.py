from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

def root(request):
    context = {
        "allbooks" : Book.objects.all()
    }
    return render(request, 'index.html', context)


def add_book(request):
    Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect('/')

def show_book(request, id):
    context = {
        "book" : Book.objects.get(id=id),
        "authors" : Author.objects.all() 
    }
    return render(request, 'bookdesc.html', context)

def add_a_b(request, id):
    book = Book.objects.get(id=id)
    author = Author.objects.get(id=request.POST['author'])
    book.authors_book.add(author)
    return redirect(f"/show_book/{book.id}")






def author(request):
    context = {
        "authors" : Author.objects.all()
    }
    return render(request, 'index2.html', context)


def add_author(request):
    Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'])
    return redirect('/author')

def show_author(request, id):
    context = {
    "books" : Book.objects.all(),
    "author" : Author.objects.get(id=id) 
    }
    return render(request, 'authors.html', context)

def add_b_a(request, id):
    author = Author.objects.get(id=id)
    book = Book.objects.get(id=request.POST['book'])
    author.books_author.add(book)
    return redirect(f"/show_author/{author.id}")