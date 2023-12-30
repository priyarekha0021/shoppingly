from django.shortcuts import render

# Create your models here.
class Student(models.Model):
 stuid=models.IntegerField()
 stuname=models.CharField(max_length=70)
 