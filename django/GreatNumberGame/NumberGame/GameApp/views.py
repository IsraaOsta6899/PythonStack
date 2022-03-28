from multiprocessing import context
from sys import flags
from xml.dom.minidom import TypeInfo
from django.shortcuts import redirect, render
import random 
def index(request):
    if 'RandomNumber' in request.session:
        request.session['RandomNumber']= request.session['RandomNumber']
    else:
        request.session['RandomNumber']=random.randint(1, 100)
    if 'flag' in request.session:
        request.session['flag']=request.session['flag']
    else:
        request.session['flag']='0'
    flag=request.session['flag']
    context={
       "flag":request.session['flag']
   }
   
    return render(request,'index.html',context)
def checkAnswer(request):
    # flag='0'
    # request.session['flag']=flag
    userInput=int(request.POST['num'])
    if userInput==request.session['RandomNumber']:
        flag='3'
        request.session['flag']=flag
        return redirect('/')
    if userInput>request.session['RandomNumber']:
        flag='2'
        request.session['flag']=flag
        return redirect('/')
    if userInput<request.session['RandomNumber']:
        flag='1'
        request.session['flag']=flag
    
    
    return redirect('/')

