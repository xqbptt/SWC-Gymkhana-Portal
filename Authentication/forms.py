from django.db.models.base import Model
from django.forms import fields
from . import models
from django import forms


class AdditionForm(forms.ModelForm):
    class Meta:
        model = models.NewEvents
        fields = ['name', 'image', 'about' ]

class MinuteForm(forms.ModelForm):
    class Meta:
        model = models.NewMinutes
        fields = ['title', 'pdf']