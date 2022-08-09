from datetime import datetime
from enum import unique
from django.views.generic import ListView
from django import forms
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

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
        txt = "{0}"
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
        txt = "{0}, {1}"
        return txt.format(self.surname, self.name)
    
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
        txt = "{0}, {1}"
        return txt.format(self.surname, self.name)
    
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


class Avatar(models.Model):
    #vinvulo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Subcarpeta avatares de media :) 
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user.username}"


def get_image_filename(instance, filename):
    title =  'titulo'
    slug = slugify(title)
    return "imagenesAvatares/%s-%s" % (slug, filename)  