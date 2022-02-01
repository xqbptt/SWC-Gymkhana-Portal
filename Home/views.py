from unicodedata import category
from django.shortcuts import render, redirect
from .models import Image, Senator, Minute, Board, Panel
# from Authentication.models import NewMinutes
from django.contrib import messages
import json
# from . import forms

# Create your views here.


def home(request):
    panels = Panel.objects.all()
    panel_list = []
    senator_dict = {}

    for panel in panels:
        senator_dict[panel.name] = Senator.objects.all().filter(panel=panel)  
        panel_list+=[panel.name]

    images = Image.objects.all()
    boards = Board.objects.all()
    context = {
        'senators':senator_dict,
        'images': images,
        'boards': boards,
    }
    context['panel_list'] = json.dumps(panel_list)
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
