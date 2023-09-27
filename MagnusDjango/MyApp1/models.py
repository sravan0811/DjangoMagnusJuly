from django.db import models

# Create your models here.
class Employee(models.Model):
    empno = models.IntegerField()
    ename = models.CharField(max_length=50)
    sal = models.IntegerField()
    deptno = models.IntegerField()

class Dept(models.Model):
    deptno = models.IntegerField()
    dname = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

class Car(models.Model):
    Brand = models.CharField(max_length=200)
    CModel = models.CharField(max_length=200)
    def __str__(self):
        return self.CModel