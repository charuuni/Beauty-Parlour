from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from Adminapp . models import *
from django.contrib import admin
from .models import *
from django.db.models import Sum
from django.contrib import messages
from datetime import datetime
from django.db.models import Q


# Create your views here.
def home(request):
    data=Branch.objects.all()
    return render(request,'home.html',{'data':data})

def serve(request,branchname):
    data=Branch.objects.all()
    
    if(branchname == 'all'):
        serv=Service.objects.all()
    else:
        serv=Service.objects.filter(branchname=branchname)
    return render(request,'service.html',{'data':data,'serv':serv})

def detail(request,service_name):
    data=Branch.objects.all()
    details=Service.objects.filter(service_name=service_name)
    return render(request,'service_detail.html',{'data':data,'details':details})

def usercontact(request):
    data = Branch.objects.all()
    return render(request,'contact.html',{'data':data})

def getData(request):
    if request.method=="POST":
        name_a = request.POST.get('name1')
        email_a= request.POST.get('email1')
        number=request.POST.get('number')
        message_a= request.POST.get('message1')

        data=Contact(name1=name_a,email1=email_a,number=number,message1=message_a)
        data.save()
        return redirect('usercontact')

def userregister(request):
    return render(request,'Register.html')
def registerdata(request):
    if request.method=="POST":
        name = request.POST.get('name1')
        email_a= request.POST.get('email')
        password_a= request.POST.get('password')
        if name== "" or email_a=="" or password_a=="":
            return redirect('userregister')
        data=Register(name=name,email=email_a,password=password_a)
        data.save()
        return redirect('login')
    
            
        
def login(request):
    return render(request,'userlogin.html')

def userlogin(request):
    if request.method == "POST":
        username=request.POST.get('name')
        password_a=request.POST.get('password')
        if Register.objects.filter(name=username,password=password_a).exists():
            data=Register.objects.filter(name=username,password=password_a).values('email','id').first()
            request.session['email'] = data['email']
            request.session['name'] = username
            request.session['password'] = password_a
            request.session['nid'] = data['id']
            return redirect('home')
        else:
            return render(request,'userlogin.html',{'msg':"invalid"})
          
    else:
        return render(request,'userlogin.html')

def logout(request):
    del request.session['email']
    del request.session['name']
    del request.session['password']
    del request.session['nid']
    return redirect('home')

def about(request):
    data = Branch.objects.all()
    return render(request,'about.html',{'data':data})



def cart(request):
    data = Branch.objects.all()
    userid = request.session.get('nid')
    key = Cart.objects.filter(userid=userid, status=0)
    
    total_price = 0
    for cart_item in key:
        total_price += cart_item.serviceid.price
    
    return render(request, 'cart.html', {'data': data,'key': key, 'total_price': total_price})


def cartdata(request, id):
    if 'nid' in request.session:
        userid=request.session.get('nid')
        price=Service.objects.get(id=id).price
        print(userid)
        key=Cart(serviceid=Service.objects.get(id=id),userid=Register.objects.get(id=userid),status=0,total=price)
        key.save()
    return redirect('cart')




def cartdelete(request,cartid):
    userid=request.session.get('nid')
    Cart.objects.filter(id=cartid,userid=userid).delete()
    return redirect('cart')    


def confirm(request):
    data = Branch.objects.all()
    return render(request,'confirm.html',{'data':data})

def booking(request):
    data = Branch.objects.all()
    userid = request.session.get('nid')
    key = Cart.objects.filter(userid=userid, status=0)
    
    total_price = 0
    for cart_item in key:
        total_price += cart_item.serviceid.price
    
    return render(request, 'booking.html', {'data': data, 'total_price': total_price, 'key': key})
    






def bookingdata(request):
    if request.method == 'POST':
        userid = request.session.get('nid')
        date = request.POST.get('date')
        time = request.POST.get('time')
        key = Cart.objects.filter(userid=userid, status=0)
        
        # Check for conflicting bookings
        conflicting_bookings = Booking.objects.filter(
            Q(date=date) & Q(time=time) & Q(cartid__serviceid__branchname__in=[item.serviceid.branchname for item in key]) &
            Q(cartid__serviceid__servicename__in=[item.serviceid.servicename for item in key])
        )
    
        if conflicting_bookings.exists():
            messages.error(request, "Another user has already booked the same service at the same time and date.")
            return redirect('booking')
           
        else:
            for item in key:
                cart_id = item.id
                user_id = userid
                booking_date = datetime.strptime(date, '%Y-%m-%d').date()
                booking_time = datetime.strptime(time, '%H:%M').time()

                data = Booking(cartid=Cart.objects.get(id=cart_id), userid=Register.objects.get(id=user_id), status=0, date=booking_date, time=booking_time)
                data.save()
                Cart.objects.filter(id=cart_id).update(status=1)

            messages.success(request, "Booking confirmed successfully")
            return redirect('confirm')
    else:
        return redirect('home')
