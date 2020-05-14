from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

#GET
def login_reg(request):
    return render(request,'index.html')

def register(request):
    print(request.POST)
    if request.method == "POST":
        errors = User.objects.create_validator(request.POST)
        if len(errors) > 0:
            print("Errors",errors)
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            pwhash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pwhash.decode())
            print("User: ", user)
            request.session['user_id'] = user.id
    return redirect('/success')

def Login(request):
    if request.method == "POST":
        user_email = User.objects.filter(email=request.POST['email'])
        if user_email:
            user = user_email[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                return redirect('/success')
            else:
                messages.error(request,"Incorrect email or password")
        else:
            messages.error(request,"Incorrect email or password")
    return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        return redirect("/")
    context = {
        'user' : User.objects.get(id=request.session['user_id']) 
    }
    return render(request, 'success.html', context )


def logout(request):
    if 'logout' in request.POST:
        del request.session['user_id']
    return redirect('/')