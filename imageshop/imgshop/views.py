from django.shortcuts import render,HttpResponseRedirect,redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import image


# Create your views here.
from imgshop.models import *

    
def home(request):

    categ=Category.objects.all()
    images=image.objects.all()
    data={'images':images,
    'categ':categ,
    }
    return render(request,'home.html',data)

def show_category(request,pkid):
    category=Category.objects.get(pk=pkid)
    categ=Category.objects.all()
    images=image.objects.filter(cate=category)
    data={'images':images,
    'categ':categ,
    }
    return render(request,'home.html',data)

def search(request):
        search=request.GET['find']
        print("search==",search)
        images=image.objects.filter(title__icontains=search)
        res={'images':images}
        return render(request,'search.html',res)

def imgresults(request):
    imgresults=image.objects.get(id=id)
    categ=image.objects.all()
    images=image.objects.filter(cate=imgresults)
    data={'images':images,
    'categ':categ
    }
    return render(request,'imgresult.html',data)


def image_like(request):
    like=0
    like=like+1
    return render(request,'home.html',{'like':like})
            