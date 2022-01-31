from django.db.models.base import Model
from django.forms import ModelForm, fields
from Authentication import models
from Home.models import Minute,About,Gallery,Senator
from django import forms


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['name', 'description']

class MinuteForm(forms.ModelForm):
    class Meta:
        model = Minute
        fields = ['title', 'pdf']

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['name', 'image', 'tag']

# class SenatorForm(forms.ModelForm):
#     class Meta:
#         model = Senator
#         fields = ['image', 'name', 'position', 'board', 'mobile', 'linked_in', 'facebook', 'email', 'address', 'tag']