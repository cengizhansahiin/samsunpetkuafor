from django.contrib import admin
from .models import PhotoLibrary
# Register your models here.

@admin.register(PhotoLibrary)
class PhotoAdmin(admin.ModelAdmin):

    list_display = ["kind","name"]
    class Meta:
        model = PhotoLibrary