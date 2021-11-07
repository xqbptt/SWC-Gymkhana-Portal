from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='gymkhana-home'),
    path('senate/', views.senate, name='gymkhana-senate'),
    path('cultural/', views.cultural, name='gymkhana-cultural'),
    path('technical/', views.technical, name='gymkhana-technical'),
    path('welfare/', views.welfare, name='gymkhana-welfare'),
    path('sports/', views.sports, name='gymkhana-sports'),
    path('hab/', views.hab, name='gymkhana-hab'),
    path('complaint/', views.complaint, name='gymkhana-complaint'),
    path('gallery.html', views.gallery, name='gymkhana-gallery'),
]

