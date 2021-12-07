# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from django.urls import path

from . import views

urlpatterns = [
  # /
  path('', views.home, name='home'),
  # TEMPORARY
  path('signin', views.sign_in, name='signin'),
  path('signout', views.sign_out, name='signout'),
  path('callback', views.callback, name='callback'),
  path('calendarAPI', views.calendarAPI, name='newevent'),
  path('userDetails', views.userDetails, name='newevent'),
  path('teamDetails', views.teamDetails, name='newevent'),
  path('formDetails', views.formDetails, name='senate-form'),
  path('MinuteDetails', views.MinuteDetails, name='minute-form'),
  
]
