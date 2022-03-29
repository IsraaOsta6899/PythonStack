from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import User
# Create your views here.
def index(request):
    context={
        "users":User.objects.all()
    }

    return render(request,'users.html',context)
def adduser(request):
    firstt=request.POST['first']
    last=request.POST['last']
    age1=int(request.POST['age'])
    email1=request.POST['email']
    newUser= User.objects.create(first_name=firstt,last_name=last,email_address=email1,age=age1)
    return redirect('/')