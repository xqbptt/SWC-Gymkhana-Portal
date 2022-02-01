from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from django.forms import ValidationError
# Create your models here.

class Minute(models.Model):
    title = models.CharField(max_length=300)
    pdf = models.FileField()

    def __str__(self):
        return self.title

class About(models.Model):
    text = models.TextField()

    def save(self, *args, **kwargs):
        if not self.pk and About.objects.exists():
        # if you'll not check for self.pk 
        # then error will also raised in update of exists model
            raise ValidationError('There is can be only one JuicerBaseSettings instance')
        return super(About, self).save(*args, **kwargs)


class Panel(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Senator(models.Model):
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=60, blank=True)
    mobile = models.CharField(max_length=20)
    linked_in = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    panel = models.ForeignKey(Panel,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name


class Board(models.Model):
    boardName = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    chairman = models.ForeignKey(Senator,on_delete=models.CASCADE)
    notices = models.TextField()
    events = models.TextField()
    announcements = models.TextField()
    url = models.URLField(default='https://swc.iitg.ac.in/stud/gymkhana')

    def __str__(self):
        return self.boardName

class Image(models.Model):
    image = models.ImageField()
