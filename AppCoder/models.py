from telnetlib import DO
from django import forms
from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    
    genre = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('O', 'Otro')
    ]
    genre = models.CharField(max_length=1,choices=genre, default='Otro')

    patId = models.IntegerField()
    mail = models.EmailField()
    tel = models.IntegerField()
    address = models.CharField(max_length=60)

    def __str__(self):
        txt="{0}, {1}"
        return txt.format(self.name, self.surname, self.genre, self.patId)
        #Luciana despues aca agregamos a los demas lo mismo para que se vea mas bonito.

class Department(models.Model):
    depId = models.IntegerField()
    name = models.CharField(max_length=40)
    mail = models.EmailField()
    tel = models.IntegerField()   

    def __str__(self):
        txt="Dpto. ID: {0} / Name: {1} / Celphone: {2} / HeadDepartment: {3}"
        return txt.format(self.depId, self.name, self.tel, self.head)

class Doctor(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)

    genre = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('O', 'Otro')
    ]
    genre = models.CharField(max_length=1,choices=genre, default='Otro')

    docId = models.IntegerField(primary_key=True)
    license = models.CharField(max_length=20)
    mail = models.EmailField()
    tel = models.IntegerField()
    address = models.CharField(max_length=60)
    specialization = models.CharField(max_length=40)
    department = Department.name

    def __str__(self):
        txt="{0} / {1} / {2} / {3} / {4}"
        return txt.format(self.name, self.surname, self.genre, self.docId, self.department)
        #Luciana despues aca agregamos a los demas lo mismo para que se vea mas bonito.

class History(models.Model):
    patient = Patient.name
    doctor = Doctor.name
    numId = models.IntegerField()