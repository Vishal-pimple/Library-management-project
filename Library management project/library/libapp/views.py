from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import books
# Create your views here.

def index(request):
    bookList = books.objects.values()

    return render(request,'index.html', {'books':bookList})

def view(request,rid):
    b=books.objects.filter(id=rid)
    content={}
    content['data']=b
    return render(request,'view.html',content)

def dashboard(request):
    b=books.objects.all()
    content={}
    content['data']=b
    return render(request,'dashboard.html',content)

def delete( request,rid):
    b=books.objects.get(id=rid)
    b.delete()
    return redirect('/')

def addbook(request):
    print(request.method)
    if request.method=='POST':
        # print("in if part")
        bNAME=request.POST['bNAME']
        bAuthor=request.POST['bAuthor']
        bLanguage=request.POST['bLanguage']
        bRelease_date=request.POST['bRelease_date']
        bbdescription=request.POST['bbdescription']
       
        #Creating objects:
        b=books.objects.create(NAME=bNAME,Author=bAuthor,Language=bLanguage,Release_date=bRelease_date)
        return redirect('/udash')

    else:
        return render(request,'addbook.html')

def edit(request,rid):
    if request.method=='POST':
        UNAME=request.POST['bNAME']
        uAuthor=request.POST['bAuthor']
        uLanguage=request.POST['bLanguage']
        uRelease_date=request.POST['bRelease_date']
        

        print("updated Name:",UNAME)
        print("updated Author:",uAuthor)
        print("updated Language:",uLanguage)
        print("updated Date:",uRelease_date)

        b=books.objects.filter(id=rid)
        b.update(NAME=UNAME,Author=uAuthor,Language=uLanguage,Release_date=uRelease_date)#update bloapp_post set title=uptitle,sdet=usdetail,pdet=updetail,cat=upcat,status=upstatus where id=rid;

        return redirect("/udash")

    else:
        b=books.objects.filter(id=rid)
        content={}
        content['data']=b
        return render(request,'editform.html',content)

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')