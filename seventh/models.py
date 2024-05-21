from django.db import models


class Student(models.Model):
    surname = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    patronymic = models.CharField(max_length=25)
    year = models.IntegerField()
    group = models.CharField(max_length=10)
