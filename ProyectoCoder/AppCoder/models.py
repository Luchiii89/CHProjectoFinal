from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=60)
    genre = models.CharField(max_length=40)
    author = models.CharField(max_length=60)
    year = models.IntegerField()
    editorial = models.CharField(max_length=30)

class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    email = models.EmailField()

class Editorial(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    tel = models.IntegerField()
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=30)

class Bookshop(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    email = models.EmailField()
    