from django.db import models

# Create your models here.

class Visit(models.Model):
    count = models.IntegerField(default=0)
