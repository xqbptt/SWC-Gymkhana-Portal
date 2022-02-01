from unicodedata import category
from django.shortcuts import render, redirect
from .models import Image, Senator, Minute, Board, Panel, About
# from Authentication.models import NewMinutes
from django.contrib import messages
import json


def home(request):
    panels = Panel.objects.all()
    panel_list = []
    senator_dict = {}

    for panel in panels:
        senator_dict[panel.name] = Senator.objects.all().filter(panel=panel)  
        panel_list+=[panel.name]

    images = Image.objects.all()
    boards = Board.objects.all()

    board_list = []
    
    for board in boards:
        board_list+=[board.id]

    minutes = Minute.objects.all()
    about = About.objects.all().first()
    context = {
        'senators':senator_dict,
        'images': images,
        'boards': boards,
        'minutes': minutes,
        'about':about,
    }
    context['panel_list'] = json.dumps(panel_list)
    context['board_list'] = json.dumps(board_list)
    return render(request, 'Home/home.html',context)


def gallery(request):
    try:
        images = Image.objects.all()
    except Image.DoesNotExist:
        pics1 = None
    context = {
        'images': images
    }
    return render(request, 'Home/gallery.html', context)
