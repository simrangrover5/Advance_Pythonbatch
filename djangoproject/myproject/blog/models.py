from django.db import models
import datetime
from users.models import AddUser

# Create your models here.
class Addblog(models.Model):
    author = models.ForeignKey(to=AddUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    blog = models.CharField(max_length=1000)
    date = models.DateField(default=datetime.datetime.now())

    def __str__(self):
        return f"{self.author}"