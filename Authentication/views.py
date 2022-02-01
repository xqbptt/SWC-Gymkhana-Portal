from django.contrib.auth.models import User
from django.contrib.auth import login # importing login
from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime, timedelta
from dateutil import tz, parser
from Authentication.auth_helper import get_sign_in_flow, get_token_from_code, store_user, remove_user_and_token, get_token
from Authentication.graph_helper import *
from django.contrib import messages
from . import forms
from Home.models import *

ALLOWED_EMAILS = ['p.shiv@iitg.ac.in']

# <HomeViewSnippet>
def home(request):
  context = initialize_context(request)
  return render(request, 'Authentication/login.html', context)
# </HomeViewSnippet>

# <InitializeContextSnippet>
def initialize_context(request):
  context = {}

  # Check for any errors in the session
  error = request.session.pop('flash_error', None)

  if error != None:
    context['errors'] = []
    context['errors'].append(error)

  # Check for user in the session
  context['user'] = request.session.get('user', {'is_authenticated': False})
  return context
# </InitializeContextSnippet>

# <SignInViewSnippet>
def sign_in(request):
  # Get the sign-in flow
  
  flow = get_sign_in_flow()
  # Save the expected flow so we can use it in the callback
  try:
    request.session['auth_flow'] = flow
  except Exception as e:
    print(e)
  # Redirect to the Azure sign-in page
  return HttpResponseRedirect(flow['auth_uri'])
# </SignInViewSnippet>

# <SignOutViewSnippet>
def sign_out(request):
  # Clear out the user and token
  remove_user_and_token(request)

  return HttpResponseRedirect(reverse('home'))
# </SignOutViewSnippet>

# <CallbackViewSnippet>
def callback(request):
  # Make the token request
  result = get_token_from_code(request)
  #Get the user's profile
  user = get_user(result['access_token'])
  if user['mail'] not in ALLOWED_EMAILS:
    return HttpResponse("You are not allowed to access this page")
  # Store user
  store_user(request, user)
  print(user)
  print(user['displayName'])
  print(user['mail'])
  try:
    user_object = User.objects.get(username = user["displayName"])
  except:
    user_object = User.objects.create(username = user['displayName'], email = user['mail'])
    user_object.save()
  #if user_object is not None: 
    #login(request,user_object)  # we call the login function to bind a user to current session, this way they get automatically logged in to django admin website
  #user_object.is_staff = True # we also need to set is_staff permission to true so that they have access to admin dashboard
  #user_object.save()
  return HttpResponseRedirect(reverse('home')) # now we just redirect to admin view, search for httpresponseredirect on django docs for more info.
# </CallbackViewSnippet>

def userDetails(request):
 
  user_objects = User.objects.all()
  current_user_object = user_objects[len(user_objects)-1]
  detail = {"name":current_user_object.name,"email":current_user_object.email}
  return JsonResponse(detail)


def AboutDetails(request):
  if request.method == 'POST':
      form = forms.AboutForm(request.POST, request.FILES)
      if form.is_valid():
        about_object = About.objects.all().first()
        about_object.text = form.text
        about_object.save()
        messages.success(request, f'Post Successful')
        return redirect('home')
  else:
      form = forms.AboutForm()
  return render(request, 'Authentication/newAddition.html', {'form': form})

def MinuteDetails(request):
  if request.method == 'POST':
      form = forms.MinuteForm(request.POST, request.FILES)
      if form.is_valid():
          form.save()
          messages.success(request, f'Post Successful')
          return redirect('home')
  else:
      form = forms.MinuteForm()
  return render(request, 'Authentication/minuteAddition.html', {'form': form})

def GalleryDetails(request):
  if request.method == 'POST':
      form = forms.GalleryForm(request.POST, request.FILES)
      if form.is_valid():
          form.save()
          messages.success(request, f'Post Successful')
          return redirect('home')
  else:
      form = forms.GalleryForm()
  return render(request, 'Authentication/galleryAddition.html', {'form': form})

def SenatorDetails(request):
  if request.method == 'POST':
      form = forms.SenatorForm(request.POST, request.FILES)
      if form.is_valid():
          form.save()
          messages.success(request, f'Post Successful')
          return redirect('home')
  else:
      form = forms.SenatorForm()
  return render(request, 'Authentication/senatorAddition.html', {'form': form})