from django.db import models

# Create your models here.
class AddUser(models.Model):
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=100,primary_key=True)
    password = models.CharField(max_length=100)
    pic = models.ImageField(upload_to='static/images')

    def __str__(self):
        return f"{self.email}"
