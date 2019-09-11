from django.db import models

# Create your models here.
class jobs(models.Model):
    name = models.CharField(max_length=20)
    job = models.CharField(max_length=100)