from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("REAPER", views.REAPER, name="REAPER"),
    path("<str:name>", views.greeting, name = "greeting")

]