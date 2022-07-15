from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    genre = models.CharField(max_length=60)
    patId = models.IntegerField()
    mail = models.EmailField()
    tel = models.IntegerField()
    address = models.CharField(max_length=60)

class Department(models.Model):
    depId = models.IntegerField()
    name = models.CharField(max_length=40)
    mail = models.EmailField()
    tel = models.IntegerField()
    head = models.CharField(max_length=60)

class Doctor(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    genre = models.CharField(max_length=60)
    docId = models.IntegerField()
    license = models.CharField(max_length=20)
    mail = models.EmailField()
    tel = models.IntegerField()
    address = models.CharField(max_length=60)
    specialization = models.CharField(max_length=40)
    department = Department.name

class History(models.Model):
    patient = Patient.name
    doctor = Doctor.name
    numId = models.IntegerField()