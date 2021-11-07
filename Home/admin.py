from Home.models import Complaints, Users
from django.contrib import admin
from .models import Complaints,Users,Events,Clubs,Boards,Achievements,Announcements

# Register your models here.

admin.site.register(Complaints)

admin.site.register(Users)

admin.site.register(Events)

admin.site.register(Clubs)

admin.site.register(Boards)

admin.site.register(Announcements)

admin.site.register(Achievements)