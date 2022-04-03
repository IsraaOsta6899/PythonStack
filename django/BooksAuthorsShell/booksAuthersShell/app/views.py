from django.shortcuts import render,HttpResponse,redirect
from .models import Author,Book

def index(request):
    context={
        'books':Book.objects.all()
    }
    return render(request,'books.html',context)
def index1(request):
    context={
        'auths':Author.objects.all()
    }
    return render(request,'authors.html',context)
def index2(request,BookID):
    context={
        'book':Book.objects.get(id=BookID),
        'auths':Author.objects.all()
    }
    return render(request,'book.html',context)
def index3(request,AuthID):
    context={
        'author':Author.objects.get(id=AuthID),
        'books':Book.objects.all()
    }
    return render(request,'author.html',context)
def addBook(request):
    Book.objects.create(title=request.POST['title'],desc=request.POST['Desc'])
    return redirect('/')
def addAuthor(request):
    Author.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'])
    return redirect('/authors')
def addauthtobook(request,BookID):
    auth_id=request.POST['auths']
    auth=Author.objects.get(id=int(auth_id))
    book=Book.objects.get(id=BookID)
    book.authors.add(auth)
    return redirect('/')


  
def addbooktoauth(request,authID):
    book_id=request.POST['books']
    book=Book.objects.get(id=int(book_id))
    auth=Author.objects.get(id=authID)
    auth.books.add(book)
    return redirect('/authors')


