
from django.db import models


class EmployeeModel(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.title




# Create your models here.
