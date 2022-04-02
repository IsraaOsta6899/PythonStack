from django.shortcuts import render, HttpResponse,redirect

from app.models import Dojo,Ninja
def index(request):
    context={
        'dojos':Dojo.objects.all(),
        
    }
    return render(request,'index.html',context)
def addNinja(request):
    ffname=request.POST['fname']
    llname=request.POST['lname']
    dojo_id=request.POST['ninjaa']
    dojo1=Dojo.objects.get(id=int(dojo_id))
    Ninja.objects.create(first_name=ffname,last_name=llname,dojo=dojo1)
    return redirect('/')




def addDojo(request):
    name1=request.POST['name']
    city1=request.POST['city']
    state1=request.POST['state']
    Dojo.objects.create(name=name1,city=city1,state=state1)
    return redirect('/')