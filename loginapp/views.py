from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required


def newlogin(request):
    return render(request,'signup.html')

@login_required(login_url='newsign')
def afterlogin(request):
    return render(request,'afterlogin.html')
def adduser(request):
    if request.method=='POST':
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        username=request.POST['uname']
        email=request.POST['email']
        password=request.POST['pwd']
        conformpassword=request.POST['cwd']
        if password==conformpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exist :)')
                return redirect('newlogin')
            else:
                user=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
                user.save()
        else:
             messages.info(request,'PASSWORD NOT MACHING :(')
             return redirect('newlogin')
        return redirect('newsign')
def newsign(request):
     return render(request,'login.html')
def addsign(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['pwd']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('afterlogin')
        else:
            messages.info(request,'INVALID USERNAME OR PASSWORD:(')
            return redirect('newsign')
        
def userlogout(request):
    auth.logout(request)
    return redirect('newsign')
    

# Create your views here.
