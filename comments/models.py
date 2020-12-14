from django.db import models

# Create your models here.

class Comments(models.Model):

    name = models.CharField(max_length=20)

    comment = models.TextField(max_length=100)

    rating = models.IntegerField(choices=[(1,'1 Yıldız'),(2,'2 Yıldız'),(3,'3 Yıldız'),(4,'4 Yıldız'),(5,'5 Yıldız')],null = True)

    created_date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name

    
    class Meta:
        ordering = ['-created_date']
