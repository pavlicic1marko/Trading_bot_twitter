from django.urls import path

from bot import views

urlpatterns = [
    path("", views.index, name="index"),

]