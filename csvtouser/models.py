from django.db import models

# Create your models here.


class UserFile(models.Model):
    filepath = models.FileField(upload_to='./userfile/')
    status = models.BooleanField(default=False)


class UserInfo(models.Model):
    name = models.CharField(max_length=100,unique=True)
    birthday =models.DateField(max_length=100)
    gender = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode =models.CharField(max_length=100)
    
    def __str__(self) :
        return self.name