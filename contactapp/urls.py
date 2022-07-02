from unicodedata import name
from django import views
from django.urls import path
from . import views
urlpatterns = [
    path("", views.Home, name="index"),
    path("add-contact/", views.addContact, name="add-contact"),
    path('profile/<str:pk>', views.Profile, name="profile"),
    path('edit-contact/<str:pk>', views.editContact, name="edit-contact"),
    path('delete-contact/<str:pk>', views.deleteContact, name="delete-contact"),
]
