from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from Employe.models import employess

from Employe.forms import Employeeform


# Create your views here.
def viewemployess(request):
    e = employess.objects.all()
    return render(request,'view.html',{'emp':e})

def home(request):
    return render(request,'home.html')

def addemployee(request):
    if (request.method=="POST"):
        i = request.POST['i']
        n = request.POST['n']
        d= request.POST['d']
        a= request.POST['a']
        e= employess.objects.create(id=i,name=n,department=d,age=a)
        e.save()
        return home(request)
    return render(request,'add.html')


def editemployee(request,n):
    e=employess.objects.get(id=n)
    if(request.method=="POST"):
        form=Employeeform(request.POST,request.FILES,instance=e)
        if form.is_valid():
            form.save()
            return home(request)
    form=Employeeform(instance=e)
    return render(request,'edit.html',{'form':form})


def delete(request,n):
    e=employess.objects.get(id=n)
    e.delete()
    return home(request)
def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        e=request.POST['e']
        f=request.POST['f']
        l=request.POST['l']

        if(cp==p):
            user=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            user.save()
            return redirect('empl:home')
        else:
            return HttpResponse("passwords are not same")
    return render(request,'register.html')



def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('empl:home')
        else:
            return HttpResponse("invalid credentials")
    return render(request,'login.html')


def details(request,n):
    e=employess.objects.get(id=n)
    return render(request,'details.html',{'emp':e})








