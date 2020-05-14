from django.shortcuts import render, HttpResponse # add HttpResponse... importants (capital H and R)

# Create your views here.

def firstFunction(request):
    return HttpResponse("Hello, World! I made my function work.")

def secondFunction(request):
    return HttpResponse("heres my second route")

def hello(request, name):
    return HttpResponse("Hello "+ name + "!")

def template(request):
    context = {
        "name": "sally",
        "numbers": [5,6,7]
    }
    return render(request, "index.html", context)
# ^^^^^ equivalent of @app.route('/')