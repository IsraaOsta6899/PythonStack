
from django.shortcuts import redirect, render
from time import gmtime, strftime
    
def index(request):
    
    if 'count' in request.session:
        if request.method=='GET':
            request.session['count']=request.session['count']+1
            return render(request,'index.html')
            
            
        else:
            if 'addtwovisits' in request.POST:
                request.session['count']=request.session['count']+1

            elif 'reset' in request.POST:
                request.session['count']=-1
            return redirect('/postt')
            
            

        
    else:
        request.session['count']=-1
        return render(request,'index.html')
def mypost(request):
    return redirect('/')
def distroy(request):
    del request.session['count']
    return render(request,'index.html')