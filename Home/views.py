from django.shortcuts import render,redirect
from .models import Complaints,Users,Events,Clubs,Boards
from django.contrib import messages
from . import forms

# Create your views here.

def home(request):
    try:
        user=Users.objects.get()
    except Users.DoesNotExist:
        user = None
    context={
        'members': user
    }
    return render(request,'Home/home.html',context)

def senate(request):
    try:
        user=Users.objects.get()
    except Users.DoesNotExist:
        user = None
    context={
        'members': user
    }
    return render(request,'Home/senate.html',context)

def cultural(request):
    try:
        board=Boards.objects.get()
    except:
        board = None
    context={
        'details': board
    }
    return render(request,'Home/cultural.html',context)    

def technical(request):
    try:
        board=Boards.objects.get()
    except:
        board = None
    context={
        'details': board
    }
    return render(request,'Home/technical.html',context) 

def welfare(request):
    try:
        board=Boards.objects.get()
    except:
        board = None
    context={
        'details': board
    }
    return render(request,'Home/welfare.html',context) 

def sports(request):
    try:
        board=Boards.objects.get()
    except:
        board = None
    context={
        'details': board
    }
    return render(request,'Home/sports.html',context) 

def hab(request):
    try:
        board=Boards.objects.get()
    except:
        board = None
    context={
        'details': board
    }
    return render(request,'Home/hab.html',context) 

def complaint(request):
    if request.method == 'POST':
        form = forms.ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Post Successful')
            return redirect('gymkhana-home')
    else:
        form = forms.ComplaintForm()
    return render(request, 'Home/complaint.html', {'form': form})

def gallery(request):
    return render(request,'Home/gallery.html')