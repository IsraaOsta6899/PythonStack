
from django.shortcuts import redirect, render
import random 
    
def index(request):
        
        if 'srt' not in request.session:
          request.session['srt']='nothing until now'
        con={
            'str':request.session['srt']
        }
        return render(request,'index.html',con)
def process_money(request):
    if 'srt' not in request.session:
        request.session['srt']=''
    if 'srt1' not in request.session:
        request.session['srt1']=''
    if 'srt2' not in request.session:
        request.session['srt2']=''
    if 'srt3' not in request.session:
         request.session['srt3']=''
    request.session['srt']=''
    
    
   

    if request.POST['which_form'] == 'Farm':
        srt=''
        if 'Farm' in request.session:
            request.session['Farm']= request.session['Farm']+random.randint(10, 20)
        else:
            request.session['Farm']=random.randint(10, 20)
        srt=srt+"you are earend "+str(request.session['Farm'])+"from Farm"
        request.session['srt']=srt
  
    elif request.POST['which_form'] == 'Cave':
        srt1=''
        if 'cave' in request.session:
            request.session['cave']= request.session['cave']+random.randint(10, 20)
        else:
            request.session['cave']=random.randint(10, 20)
        srt1=srt1+"you are earend "+str(request.session['cave'])+"from cave"
        request.session['srt1']=srt1
        
    elif request.POST['which_form'] == 'House':
        srt2=''
        if 'House' in request.session:
            request.session['House']= request.session['House']+random.randint(10, 20)
        else:
            request.session['House']=random.randint(10, 20)
        srt2=srt2+"you are earend "+str(request.session['House'])+"from House"
        request.session['srt2']=srt2
        
    else:
        srt3=''
        flag=random.randint(0, 1)
        if flag ==0:
            if 'Casino' in request.session:
                request.session['Casino']= request.session['Casino']+random.randint(10, 20)
                srt3=srt3+"you are earend "+str(request.session['Casino'])+"from Casino"
                
            else:
                request.session['Casino']=random.randint(10, 20)
                srt3=srt3+"you are earend "+str(request.session['Casino'])+"from Casino"

        elif flag==1:
            if 'Casino' in request.session:
                request.session['Casino']= request.session['Casino']+-1*(random.randint(10, 20))
                srt3=srt3+"you are lost "+str(request.session['Casino'])+"from Casino"
            else:
                request.session['Casino']=random.randint(10, 20)
                srt3=srt3+"you are lost "+str(request.session['Casino'])+"from Casino"

        
        request.session['srt3']=srt3
    request.session['srt']=request.session['srt']+'\n'+request.session['srt1']+'\n'+request.session['srt2']+'\n'+request.session['srt3']
    return redirect('/')
        