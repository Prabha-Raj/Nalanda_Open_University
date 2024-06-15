from django.db import models

# Create your models here.
class Program(models.Model):
    program=models.CharField(max_length=100)
class Branch(models.Model):
    branch=models.CharField(max_length=100)
class Year(models.Model):
    year=models.CharField(max_length=100)   
class Material(models.Model):
    ids=models.AutoField(primary_key=True)
    program=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    file_name=models.CharField(max_length=255)
    my_file=models.FileField(upload_to='')

class News(models.Model):
    nid=models.AutoField(primary_key=True)
    newstext=models.TextField()
    newsdate=models.CharField(max_length=30)