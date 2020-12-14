from django.shortcuts import render,redirect
from photolibrary.models import PhotoLibrary
from comments.models import Comments
from django.contrib import messages
from django.db import models


def mainpage(request):
    comments = Comments.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        rating = request.POST.get("rating")
        if rating:
            pass
        else:
            messages.warning(request,"Lütfen oy verdiğinizden emin olun ve lütfen tekrar deneyin.")
            return redirect("/")
        comment = request.POST.get("comment")
        newComment = Comments(name = name,comment=comment,rating=rating)
        newComment.save()


    return render(request,"mainpage.html",{"comments":comments})

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def location(request):
    return render(request,"location.html")