from django.urls import path
from . import views

urlpatterns = [
    path('meetups_app/', views.index)
]
