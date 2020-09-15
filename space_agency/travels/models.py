from django.db import models

# Create your models here.
class Travel(models.Model):
        destination = models.CharField(max_length=200)
        arrival_time = models.DateTimeField()
        departure_time = models.DateTimeField()
        image = models.ImageField()