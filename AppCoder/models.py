from datetime import datetime
from enum import unique
from pyexpat import model
from tabnanny import verbose
from django.views.generic import ListView
from django import forms
from django.db import models


# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    #dni = models.CharField(max_length=10, unique=True,verbose_name='Dni')
    #date_creation = models.DateTimeField(auto_now=True,verbose_name="Fecha Registro") #la fecha en que se registro
    #age =  models.PositiveIntegerField(default=True) #vamos a cargar la edad 
    age = models.DateField(default=datetime.now,verbose_name="Fecha Nacimiento") #otra forma de cargar la edad
    avatar = models.ImageField(height_field=None, width_field=None, max_length=None,upload_to='avatar/%Y/%m/%d',null=True,blank=True)
    personal_files = models.FileField(upload_to='avatar/%Y/%m/%d',null=True,blank=True)
    genre = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('O', 'Otro')
    ]
    genre = models.CharField(max_length=1,choices=genre,default='O')
    patId = models.IntegerField()
    mail = models.EmailField()
    tel = models.IntegerField()
    address = models.CharField(max_length=60)

    def __str__(self):
        txt="Apellido y Nombre: {0}, {1} //// Genero {2} //// PatientID: {3} //// {4}"
        return txt.format(self.surname, self.name, self.genre, self.patId, self.age)

# class Meta:
#     db_table = 'pacientes'
#     verbose_name = 'Paciente'
#     verbose_name_plurar = 'Pacientes'
#     ordering = ['id'] #lo ordenamos ascendentes por id, si queremos descendente -id

class Department(models.Model):
    depId = models.IntegerField()
    name = models.CharField(max_length=40)
    mail = models.EmailField()
    tel = models.IntegerField()   

    def __str__(self):
        txt="Dpto. ID: {0} //// Name: {1} //// Cell-Phone: {2} //// E-Mail: {3}"
        return txt.format(self.depId, self.name, self.tel, self.mail)

class Doctor(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)

    genre = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('O', 'Otro')
    ]
    genre = models.CharField(max_length=1,choices=genre,default='O')
    docId = models.IntegerField(primary_key=True)
    license = models.CharField(max_length=20)
    mail = models.EmailField()
    tel = models.IntegerField()
    address = models.CharField(max_length=60)
    specialization = models.CharField(max_length=40)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        txt="AyN: {0}, {1} //// Genre: {2} //// ID: {3} //// Department: {4}"
        return txt.format(self.name, self.surname, self.genre, self.docId, self.department)

class History(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    numId = models.IntegerField(primary_key=True)
    histo = models.CharField(max_length=360)