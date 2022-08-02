from datetime import datetime
from enum import unique
from pyexpat import model
from tabnanny import verbose
from django.views.generic import ListView
from django import forms
from django.db import models
from django.urls import reverse
from rsa import PrivateKey

# Create your models here.
class Department(models.Model):
    """
    Modelo que representa un departamento o especialidad del hospital.
    """
    name = models.CharField(max_length=40, verbose_name='Nombre')
    mail = models.EmailField(verbose_name='Email')
    tel = models.IntegerField(verbose_name='Teléfono')   
    head_of = models.CharField(max_length=60, verbose_name='Jefe Dpto') #director del departamento.

    def __str__(self):
        """
        Cadena para representar el objeto Department
        """
        txt = "Nombre: {0}"
        return txt.format(self.name)


class Doctor(models.Model):
    """
    Modelo que representa un doctor.
    """
    name = models.CharField(max_length=60, verbose_name='Nombre')
    surname = models.CharField(max_length=60, verbose_name='Apellido')
    genre = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('O', 'Otro')
    ]
    genre = models.CharField(max_length=1,choices=genre,default='O', verbose_name='Género')
    DNI = models.IntegerField(primary_key=True,unique=True, verbose_name='DNI')
    license = models.CharField(max_length=20, verbose_name='Matrícula')
    mail = models.EmailField(verbose_name='Email')
    tel = models.IntegerField(verbose_name='Telefono')
    address = models.CharField(max_length=60, verbose_name='Dirección')
    department = models.ForeignKey(Department,on_delete=models.CASCADE, verbose_name='Departamento')
    
    def __str__(self):
        """
        Cadena para representar el objeto Doctor
        """
        txt = "Apellido y Nombre: {0}, {1} //// DNI: {2} //// Matrícula: {3} //// Department: {4}"
        return txt.format(self.name, self.surname, self.DNI, self.license, self.department.name)
    
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de Doctor.
        """
        return reverse('listDoctor')
        #return reverse('model-detail-view', args=[str(self.id)]) LUEGO CAMBIAR POR ALGO SIMILAR A ESTO


class Patient(models.Model):
    """
    Modelo que representa un paciente.
    """
    name = models.CharField(max_length=60, verbose_name='Nombre')
    surname = models.CharField(max_length=60, verbose_name='Apellido')
    genre = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('O', 'Otro')
    ]
    genre = models.CharField(max_length=1,choices=genre,default='O', verbose_name='Género')
    DNI = models.IntegerField(primary_key=True, unique=True, verbose_name='DNI')
    register_date = models.DateField(default=datetime.now,verbose_name="Fecha de registro") 
    birth_date = models.DateField(verbose_name="Fecha de nacimiento") #otra forma de cargar la edad
    photo = models.ImageField(height_field=None, width_field=None, max_length=None,upload_to='avatar/%Y/%m/%d',null=True,blank=True, verbose_name='Imágen de Perfil')
    personal_files = models.FileField(upload_to='avatar/%Y/%m/%d',null=True,blank=True, verbose_name='Archivos')
    mail = models.EmailField(verbose_name='Email')
    tel = models.IntegerField(verbose_name='Telefono')
    address = models.CharField(max_length=60, verbose_name='Dirección')
    
    def __str__(self):
        """
        Cadena para representar el objeto Patient
        """
        txt = "Apellido y Nombre: {0}, {1} //// DNI {2} //// Teléfono: {3} //// Mail: {4}"
        return txt.format(self.surname, self.name, self.DNI, self.tel, self.mail)
    
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de Patient.
        """
        return reverse('listPatient')
        #return reverse('model-detail-view', args=[str(self.id)]) LUEGO CAMBIAR POR ALGO SIMILAR A ESTO


class History(models.Model):
    """
    Modelo que representa una historia clínica.
    """
    nro = models.IntegerField(primary_key=True, unique=True, verbose_name="nro_history")
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date = models.DateField()
    comments = models.TextField(max_length=360)
     
    def __str__(self):
        """
        Cadena para representar el objeto History
        """
        txt = "{0} //// Doctor: {1} //// Date: {2}"
        return txt.format(self.patient, self.doctor, self.date)