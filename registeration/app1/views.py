#from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def Home(request):
    return render(request, 'home.html')
def Signup(request):

    if request.method == 'POST':
        uname=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']

        if pass1!=pass2:
            return HttpResponse("Passwords dont match")
        else:
            myuser=User.objects.create_user(uname,email,pass1)
            myuser.save()
            return redirect('login')

        if User.objects.filter(username = uname).first():
            messages.error(request, "This username is already taken")
            return redirect('signup')

    return render(request, 'signup.html')

def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['pass']

        user=authenticate(request,username=username,password=pass1)
        
        if user is not None:
            login(request,user)
            username=user.username
            return render(request,'home.html', {'username':username})
            #return redirect('home',{'username':username})
        else:
            return HttpResponse("Credentials entered arent correct")
        






    return render(request, 'login.html')

def Logout(request):
    logout(request)
    return redirect('login')