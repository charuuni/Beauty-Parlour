from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import admin
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.http import JsonResponse
from Userapp . models import *
from django.contrib import admin






# Create your views here.
def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username = username, password = password)
 
        if user is not None:
           auth.login(request,user)
           return redirect('adminindex')
        else:
            messages.error(request,'Invalid Username or Password')
            return redirect('adminlogin')
     
    else:
        return render(request,'adminlogin.html')
    

    
def adminindex(request):
    user_s=Register.objects.all().count()
    appointment_s=Booking.objects.all().count()
    contact1=Contact.objects.all().count()
    return render(request,'adminindex.html',{'Register':user_s,'Booking':appointment_s,'Contact':contact1})
   
def addbranches(request):
    return render(request, 'addbranches.html')
def branchdata(request):
    if request.method=="POST":
        branchname=request.POST.get('branchname')
        description=request.POST.get('description')
        image=request.FILES['image']
        

        data=Branch(branchname=branchname,description=description,image=image)
        data.save()
        return redirect('viewbranches')

def viewbranches(request):
    data=Branch.objects.all()
    return render(request, 'viewbranches.html', {'key':data})
def edit(request,id):
    data=Branch.objects.filter(id=id)
    return render(request,'edit.html',{'data':data})       
def update(request,id):
    if request.method=='POST':
        branchname=request.POST['branchname']
        description=request.POST['description']
       
        try:
            image=request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(image.name, image)
        except MultiValueDictKeyError:
            file =Branch.objects.get(id=id).image
            
        data=Branch.objects.filter(id=id).update(branchname=branchname,description=description,image=file)
        return redirect('viewbranches')
        
def delete(request,id):
    data=Branch.objects.filter(id=id).delete()
    return redirect('viewbranches')

def addservice(request):
    data=Branch.objects.all()
    return render(request, 'addservice.html', {'data':data})
   
def servicedata(request):
    if request.method=="POST":
        servicename=request.POST.get('servicename')
        branchname=request.POST.get('branchname')
        price=request.POST.get('price')
        image=request.FILES['image']
        service_name=request.POST.get('service_name')
        service_type=request.POST.get('service_type')
        
        data=Service(servicename=servicename,branchname=branchname,price=price,image=image,service_name=service_name,service_type=service_type)
        data.save()
        return redirect('viewservice')
        
def viewservice(request):
    data=Service.objects.all()
    return render(request, 'viewservice.html', {'data':data})
def editservice(request,id):
    data=Service.objects.filter(id=id)
    branch=Branch.objects.all()
    service=Service.objects.all()
    return render(request,'editservice.html',{'data':data,'branch':branch, 'service':service} )  
def updates(request,id):
    if request.method=='POST':
        servicename=request.POST['servicename']
        branchname=request.POST['branchname']
        price=request.POST['price']
        service_name=request.POST.get('service_name')
        service_type=request.POST.get('service_type')
       
        try:
            image=request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(image.name, image)
        except MultiValueDictKeyError:
            file =Service.objects.get(id=id).image
            
        data=Service.objects.filter(id=id).update(servicename=servicename,branchname=branchname,price=price,image=image,service_name=service_name,service_type=service_type)
        return redirect('viewservice')
        
def delete(request,id):
    data=Service.objects.filter(id=id).delete()
    return redirect('viewservice')

def viewcontact(request):
    data=Contact.objects.all()
    return render(request,'viewcontact.html',{'data':data})

def users(request):
    data=Register.objects.all()
    return render(request,'user.html',{'data':data})

def booking_list(request):
    booklist = Booking.objects.all()
    return render(request, 'booking_list.html', {'booklist': booklist})









