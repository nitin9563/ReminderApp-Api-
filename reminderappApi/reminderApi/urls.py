from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path("info/", views.Reminders.as_view())

]