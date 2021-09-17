from django.db import models

# Create your models here.


class Destination(models.Model):
    type = models.CharField(max_length=100, default="")
    desc = models.TextField(default="")
    img = models.ImageField(upload_to='pics', default="")
    brand = models.CharField(max_length=50, default="")
