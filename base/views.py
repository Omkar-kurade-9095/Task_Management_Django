from django.shortcuts import render,redirect

from .models import Task,HistoryModel

# Create your views here.


def home(request):
    a=Task.objects.all()
    
    return render(request,'home.html',{'a':a})


def addtask(request):
    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        Task.objects.create(title=title,desc=desc)
        return redirect('home')
    
    return render(request,'addtask.html')

def edit(request,id):
    
    a=Task.objects.get(id=id)
    
    if request.method =='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        print(title,desc)
        a.title=title
        a.desc=desc
        a.save()
        return redirect('home')
  
    return render(request,'addtask.html',{'a':a})
    
    
def delete(request,id):
    
    a=Task.objects.get(id=id)
    if request.method == 'POST':
        HistoryModel.objects.create(title=a.title,desc=a.desc)
        a.delete()
        return redirect('home')

    return render(request,'delete.html',{'a':a})
        

def details(request,id):
    a=Task.objects.get(id=id)
    
    return render(request,'details.html',{'a':a})


def history(request):
    
    a=HistoryModel.objects.all()
    
    return render(request,'history.html',{'a':a})


def historydel(request,id):
    a=HistoryModel.objects.get(id=id)
    a.delete()
    return redirect('history')

def clear(request):
    a=HistoryModel.objects.all()
    a.delete()
    return redirect('history')
    
    
    
def restore(request,id):
    a=HistoryModel.objects.get(id=id)
    Task.objects.create(title=a.title,desc=a.desc)
    a.delete()
    return redirect('home')
    
    
def Restoreall(request):
    
    a=HistoryModel.objects.all()
    
    for i in a:
        print(i.title,i.desc)
        Task.objects.create(title=i.title,desc=i.desc)
    
    a.delete()
    
    
    return redirect('home')
    
    
    