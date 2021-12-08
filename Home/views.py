from django.shortcuts import render, redirect
from .models import Complaint, Senator, Event, Club, Board
# from Authentication.models import NewMinutes
from django.contrib import messages
from . import forms

# Create your views here.


def home(request):
    # try:
    #     user = Users.objects.get()
    # except Users.DoesNotExist:
    #     user = None
    # context = {
    #     'members': user
    # }
    return render(request, 'Home/home.html')


def senate(request):
    # try:
    #     mins = NewMinutes.objects.get()
    # except NewMinutes.DoesNotExist:
    #     mins = None
    # context = {
    #     'minutes': mins
    # }
    return render(request, 'Home/senate.html')


def cultural(request):
    try:
        board = Board.objects.get()
    except:
        board = None
    context = {
        'details': board
    }
    return render(request, 'Home/cultural.html', context)


def technical(request):
    try:
        board = Board.objects.get()
    except:
        board = None
    context = {
        'details': board
    }
    return render(request, 'Home/technical.html', context)


def welfare(request):
    try:
        board = Board.objects.get()
    except:
        board = None
    context = {
        'details': board
    }
    return render(request, 'Home/welfare.html', context)


def sports(request):
    try:
        board = Board.objects.get()
    except:
        board = None
    context = {
        'details': board
    }
    return render(request, 'Home/sports.html', context)


def hab(request):
    try:
        board = Board.objects.get()
    except:
        board = None
    context = {
        'details': board
    }
    return render(request, 'Home/hab.html', context)


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
    return render(request, 'Home/gallery.html')


def Senators(request):
    return render(request, 'Home/Senators.html')
