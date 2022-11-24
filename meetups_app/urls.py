from django.urls import path
from . import views

urlpatterns = [
    path('meetups_app/', views.index),
    path('meetups_app/<slug:meetup_slug>', views.meetup_details),
]
