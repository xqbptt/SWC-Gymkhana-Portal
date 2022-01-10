from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.fields import TextField
# Create your models here.

class Minute(models.Model):
    title = models.CharField(max_length=300)
    pdf = models.FileField()

    def __str__(self):
        return self.title

class About(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    def __str__(self):
        return self.name


class Senator(models.Model):
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=60, blank=True)
    board = models.ForeignKey('Panel',on_delete=models.CASCADE,null=True)
    mobile = models.CharField(max_length=20)
    linked_in = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    tag = models.IntegerField(null=True,help_text="0 for adosa,1 for senators,2 for UGs,3 for PGs,4 for Girls")
    def __str__(self):
        return self.name

class Panel(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Board(models.Model):
    id = models.CharField(primary_key=True,max_length=40)
    boardName = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    position = models.CharField(max_length=40)
    notices = models.TextField()
    events = models.TextField()
    announcements = models.TextField()

    def __str__(self):
        return self.name

class Gallery(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField()
    tag = models.IntegerField(null=True)

    def __str__(self):
        return self.name