from . import models
from django import forms


class AdditionForm(forms.ModelForm):
    class Meta:
        model = models.NewEvents
        fields = ['name', 'image', 'about' ]