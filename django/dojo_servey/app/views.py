
from django.shortcuts import render
from time import gmtime, strftime
    
def index(request):
    
    return render(request,'index.html')
def result(request):
    
    name = request.POST['Name']
    location = request.POST['Location']
    language = request.POST['Language']
    comment=request.POST['Comment']
    context = {
    	"name" : name,
    	"location" : location,
        "language":language,
        "comment":comment

    }
   
    return render(request,'show.html',context)

