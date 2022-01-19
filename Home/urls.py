from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='gymkhana-home'),
    path('senate/', views.senate, name='gymkhana-senate'),
    path('gallery.html', views.gallery, name='gymkhana-gallery'),
    path('Senators.html', views.Senators, name='gymkhana-Senators'),
]
