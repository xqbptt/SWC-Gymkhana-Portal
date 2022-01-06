from django.shortcuts import render, redirect
from .models import Gallery,Senator,Minute
# from Authentication.models import NewMinutes
from django.contrib import messages
# from . import forms

# Create your views here.


def home(request):
    try:
        sr = Senator.objects.all().filter(tag=1)
        images = Gallery.objects.all()
        ads = Senator.objects.all().filter(tag=0)
    except Senator.DoesNotExist:
        sr = None
    context = {
        'reps': sr,
        'dean': ads,
        'images': images
    }
    return render(request, 'Home/home.html',context)


def senate(request):
    try:
        sr = Senator.objects.all().filter(tag=1)
        ug = Senator.objects.all().filter(tag=2)
        pg = Senator.objects.all().filter(tag=3)
        gs = Senator.objects.all().filter(tag=4)
        ms = Minute.objects.all()
        ads = Senator.objects.all().filter(tag=0)
    except Senator.DoesNotExist:
        sr = None
    context = {
        'reps': sr,
        'ugs':ug,
        'pgs':pg,
        'girls':gs,
        'mins':ms,
        'dean':ads
    }
    return render(request, 'Home/senate.html',context)


def cultural(request):
    
    return render(request, 'Home/cultural.html')


def technical(request):
    
    return render(request, 'Home/technical.html')


def welfare(request):
    
    return render(request, 'Home/welfare.html')


def sports(request):

    return render(request, 'Home/sports.html')


def hab(request):
    
    return render(request, 'Home/hab.html')


def gallery(request):
    try:
          images = Gallery.objects.all()
    except Gallery.DoesNotExist:
        pics1 = None
    context = {
        'images': images
    }
    return render(request, 'Home/gallery.html', context)


def Senators(request):
    return render(request, 'Home/Senators.html')
