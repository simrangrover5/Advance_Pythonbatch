from django.db import models
import datetime

# Create your models here.
class Addblog(models.Model):
    title = models.CharField(max_length=100)
    blog = models.CharField(max_length=1000)
    date = models.DateField(default=datetime.datetime.now())