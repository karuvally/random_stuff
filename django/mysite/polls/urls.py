from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("easter", views.easter_eggs, name="easter")
]

