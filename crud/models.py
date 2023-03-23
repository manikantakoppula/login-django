from django.db import models
import datetime

class Department(models.Model):
    department = models.CharField(max_length=100)
    def __str__(self) :
        return self.department

class Employee(models.Model):
    e_name = models.CharField(max_length=100)
    e_salary = models.BigIntegerField()
    address = models.TextField(max_length=400)
    created_now = models.DateTimeField(default=datetime.datetime.now())
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self) :
        return self.e_name
    

