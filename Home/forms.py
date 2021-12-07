from . import models
from django import forms


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = models.Complaint
        fields = ['name', 'webmail', 'complaint' ]