from django.shortcuts import render, redirect
from .models import Gallery,Senator,Minute
# from Authentication.models import NewMinutes
from django.contrib import messages
# from . import forms

# Create your views here.


def home(request):
    try:
        sr = Senator.objects.all().filter(tag=1)
        ads = Senator.objects.all().filter(tag=0)
    except Senator.DoesNotExist:
        sr = None
    context = {
        'reps': sr,
        'dean': ads
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
        pics1 = Gallery.objects.all().filter(tag=1)
        pics2 = Gallery.objects.all().filter(tag=2)
        pics3 = Gallery.objects.all().filter(tag=3)
        pics4 = Gallery.objects.all().filter(tag=4)
    except Gallery.DoesNotExist:
        pics1 = None
    context = {
        'img1': pics1,
        'img2': pics2,
        'img3': pics3,
        'img4': pics4
    }
    return render(request, 'Home/gallery.html', context)


def Senators(request):
    return render(request, 'Home/Senators.html')
