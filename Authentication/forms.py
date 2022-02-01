from django.db.models.base import Model
from django.forms import ModelForm, fields
from Authentication import models
from Home.models import Minute,About,Image,Senator
from django import forms


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['text']

class MinuteForm(forms.ModelForm):
    class Meta:
        model = Minute
        fields = ['title', 'pdf']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']

# class SenatorForm(forms.ModelForm):
#     class Meta:
#         model = Senator
#         fields = ['image', 'name', 'position', 'board', 'mobile', 'linked_in', 'facebook', 'email', 'address', 'tag']