from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.photolibrary,name="photolibrary"),
    path("photolibrary/<str:kind>",views.kindphotolibrary,name = "kindphotolibrary"),

]