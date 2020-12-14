from django.db import models
from django import forms
# Create your models here.
kind_choices = [('Poodle','Poodle'),('Pomeranian','Pomeranian'),('Shih Tzu','Shih Tzu'),('Yorkshire Terrier','Yorkshire Terrier'),('Maltese Terrier','Maltese Terrier'),('Minyatür Schnauzer','Minyatür Schnauzer')]

class PhotoLibrary(models.Model):

    kind = models.CharField(max_length=20,choices=kind_choices)
    name = models.CharField(max_length=20)
    photo = models.ImageField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.kind




