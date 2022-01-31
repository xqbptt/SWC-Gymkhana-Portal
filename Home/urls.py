from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='gymkhana-home'),
    path('gallery.html', views.gallery, name='gymkhana-gallery'),
]
