from django.shortcuts import render,redirect
from django.contrib import messages
from app1.models import Product

# Create your views here.
def Showindex(request):
    res=Product.objects.all()
    return render(request,"index.html",{"data":res})
def saveproducts(request):
    na=request.POST.get("p1")
    pr=request.POST.get("p2")
    qu=request.POST.get("p3")
    pic=request.FILES["p4"]
    file = request.FILES["p5"]
    Product(Name=na,Price=pr,Quantity=qu,Picture=pic,file=file).save()
    messages.success(request,"Product saved succesfully")
    return redirect('main')
def update(request):
    id=request.GET.get("id")
    value=Product.objects.get(idno=id)
    return render(request,"update.html",{"value":value})
def updateproduct(request):
    id=request.POST.get("d1")
    na=request.POST.get("d2")
    pr=request.POST.get("d3")
    qua=request.POST.get("d4")
    img=request.FILES["d5"]
    Product.objects.filter(idno=id).update(Name=na,Price=pr,Quantity=qua,Picture=img)
    #result=Product.objects.get(idno=id)
    return redirect('main')

    #return render(request,"index.html",{"data":result})
def delete(request):
    id=request.GET.get("id")
    Product.objects.get(idno=id).delete()
    return redirect('main')

