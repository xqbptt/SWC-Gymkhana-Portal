from django.db import models
from django.db.models.base import Model

# Create your models here.

class Complaints(models.Model):
    name = models.CharField(max_length=30)
    webmail = models.EmailField()
    complaint = models.TextField()

    def __str__(self):
        return self.name

class Users(models.Model):
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    board = models.CharField(max_length=30)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name

class Events(models.Model):
    name = models.TextField()
    image = models.ImageField()
    about = models.TextField()

    def __str__(self):
        return self.name

class Clubs(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField()
    about = models.TextField()
    aim = models.TextField()
    activities = models.TextField()
    acheivements = models.TextField()
    secretary = models.ForeignKey(Users,on_delete=models.CASCADE)
    pastEvents = models.TextField()

    def __str__(self):
        return self.name


class Boards(models.Model):
    name = models.CharField(max_length=30)
    logo= models.ImageField()
    icon = models.ImageField()
    about = models.TextField()
    chairman = models.ForeignKey(Users,on_delete=models.CASCADE)
    event = models.ForeignKey(Events,on_delete=models.CASCADE)
    club = models.ForeignKey(Clubs,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Announcements(models.Model):
    title = models.TextField()
    date = models.DateTimeField()
    mark = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Achievements(models.Model):
    title = models.TextField()
    description = models.TextField()
    image = models.ImageField()
    year = models.IntegerField()

    def __str__(self):
        return self.title