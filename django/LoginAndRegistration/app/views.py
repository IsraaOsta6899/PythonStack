from django.shortcuts import render,HttpResponse,redirect
from app.models import User
from django.contrib import messages
from app import models

# Create your views here.
def index(request):

    return render(request,'LoginAndRegistration.html')
def registration(request):
    errors = User.objects.registration_validator(request.POST)
        
    if len(errors) > 0:
        context={
            'flag':0
        }
       
        for key, value in errors.items():
            messages.error(request, value)
        
        return render(request, 'LoginAndRegistration.html',context)
    else:
        models.register(request.POST)
        return render(request,'LoginAndRegistration.html')
def login(request):
    errors2 = User.objects.login_validator(request.POST)
        
    if len(errors2) > 0:
        context={
            'flag':1
        }
       
        for key, value in errors2.items():
            messages.error(request, value)
       
        return render(request, 'LoginAndRegistration.html',context)
    else:
        flag=models.confermLogin(request.POST)
        if(flag):
            context={
                'user':User.objects.get(email=request.POST['email'])
            }
            return render(request,'sucsess.html',context)
        else:
            return redirect('/')