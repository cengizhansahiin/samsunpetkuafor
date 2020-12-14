from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import PhotoLibrary
# Create your views here.

def photolibrary(request):

    form = PhotoLibrary.objects.all()

    return render(request,"photolibrary.html",{'form':form})
def kindphotolibrary(request,kind):

    form = PhotoLibrary.objects.filter(kind = kind)



    return render(request,"kindphotolibrary.html",{'form':form,"kind":kind})
