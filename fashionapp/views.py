from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Fashion
from . form import fashionform

# Create your views here.
def index(request):
    fashion= Fashion.objects.all()
    context={'fashion_list':fashion}
    return render(request,'index.html',context)

def details(request,fashion_id):
    fashion= Fashion.objects.get(id=fashion_id)
    return render(request,'details.html',{'fashion':fashion})
def add_fashion(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        price = request.POST.get('price',)
        img = request.FILES['img']
        fashion=Fashion(name=name,desc=desc,price=price,img=img)
        fashion.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    fashion=Fashion.objects.get(id=id)
    form=fashionform(request.POST or None,request.FILES,instance=fashion)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'fashion':fashion})
def delete(request,id):
    if request.method=='POST':
        fashion=Fashion.objects.get(id=id)
        fashion.delete()
        return redirect('/')
    return render(request,'delete.html')
