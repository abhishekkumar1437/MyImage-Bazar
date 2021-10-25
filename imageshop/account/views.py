from django.contrib import auth
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages
from imgshop.models import image
from imageshop.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
from .models import signup_user

# Create your views here.

"""-------------signup function ------------"""
"""
def signup(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
       
        if password==cpassword:
            if signup_user.objects.filter(email=email).exists():
                messages.error(request,'Email already exist!! Please signin!!')
                return redirect('signup')
            else:
                user=signup_user(name=name,email=email,password=password,cpassword=cpassword)
                user.save()
                print("sent to database")
                messages.info(request,'User created')
                return redirect('signin')
        else:
            messages.error(request,'Password not matching')
            return redirect('signup')  
    else:
        return render(request,'signup.html')





def signin(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']

        user = signup_user.get(email=email,password=password)
        print("error")
        print(user)
        if user is not None:
            return redirect('/')     
        else:
            messages.info(request,'Invalid username or password')
            return redirect('signin')
    else:
        return render(request,'signin.html')
"""


def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            print("1")
            return redirect('/')
        else:
            messages.info(request,'Invalid username or password')
            print(user)
            return redirect('signin')
    

    else:
        return render(request,'signin.html')



def signup(request):

    if request.method == 'POST':
        username=request.POST['username']
        first_name= request.POST['first_name']
        email = request.POST['email']
        password= request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(email=email).exists():
                messages.error(request,'Email already registered')
                return redirect('signup')
           
            else: 
                if User.objects.filter(username=username).exists():
                    messages.error(request,'Username Taken')
                    return redirect('signup')
                else:   
                    user = User.objects.create_user(username=username,first_name=first_name,email=email,password=password)
                    user.save()
                    messages.info(request,'User Created')
                    return redirect('signin')
        else:        
            messages.error(request,'Password not matching')
            return redirect('signup')
        return redirect('/')

    else:
      return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def search(request):
        search=request.GET['find']
        print("search==",search)
        images=image.objects.filter(title__icontains=search)
        res={'images':images}
        return render(request,'search.html',res)

def pay(request):
    idz=37
    return render(request,'pay.html',{'idz':idz})

def cart(request):
    return render(request,'cart.html')