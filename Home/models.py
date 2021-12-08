from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField()
    about = models.TextField()

    def __str__(self):
        return self.name

class Minute(models.Model):
    title = models.CharField(max_length=300)
    pdf = models.FileField()

    def __str__(self):
        return self.title

class Complaint(models.Model):
    name = models.CharField(max_length=30)
    webmail = models.EmailField()
    complaint = models.TextField()

    def __str__(self):
        return self.name

class Senator(models.Model):
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=60)
    mobile = models.CharField(max_length=20)
    linked_in = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.TextField()
    image = models.ImageField()
    about = models.TextField()

    def __str__(self):
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField()
    about = models.TextField()
    aim = models.TextField()
    activities = models.TextField()
    acheivements = models.TextField()
    secretary = models.ForeignKey(Senator,on_delete=models.CASCADE)
    pastEvents = models.TextField()

    def __str__(self):
        return self.name


class Board(models.Model):
    name = models.CharField(max_length=30)
    logo= models.ImageField()
    icon = models.ImageField()
    about = models.TextField()
    chairman = models.ForeignKey(User,on_delete=models.CASCADE)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    club = models.ForeignKey(Club,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Announcement(models.Model):
    title = models.TextField()
    date = models.DateTimeField()
    mark = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Achievement(models.Model):
    title = models.TextField()
    description = models.TextField()
    image = models.ImageField()
    year = models.IntegerField()

    def __str__(self):
        return self.title