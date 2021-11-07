from . import models
from django import forms


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = models.Complaints
        fields = ['name', 'webmail', 'complaint' ]