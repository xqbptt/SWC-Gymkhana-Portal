from unicodedata import category
from django.shortcuts import render, redirect
from .models import Gallery,Senator,Minute,Board,Panel
# from Authentication.models import NewMinutes
from django.contrib import messages
import json
# from . import forms

# Create your views here.


def home(request):
    panels = Panel.objects.all()
    senator_dict = {}
    for category in panels:
        senator_dict[category.name] = Senator.objects.all().filter(panel=category)  
    images = Gallery.objects.all()
    boards = Board.objects.all()
    board_list = []
    for board in boards:
        board_list += [board.id]
    print(board_list)

    context = {
        'senators':senator_dict,
        'images': images,
        'boards': boards,
    }
    context['board_list'] = json.dumps(board_list)
    print(type(context['board_list']))
    
    return render(request, 'Home/home.html',context)


def gallery(request):
    try:
          images = Gallery.objects.all()
    except Gallery.DoesNotExist:
        pics1 = None
    context = {
        'images': images
    }
    return render(request, 'Home/gallery.html', context)
