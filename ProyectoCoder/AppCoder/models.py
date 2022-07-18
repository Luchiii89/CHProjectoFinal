from time import time
from django.db import models
from django.utils import timezone
# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    IdNumber = models.CharField(max_length=20, unique=True)
    birthDate = models.DateField()
    genre = models.CharField(max_length=60)
    mail = models.EmailField()
    tel = models.IntegerField()
    address = models.TextField(blank=True)
    medicalRecords = models.TextField(blank=True, default='None')
    allergies = models.TextField(blank=True, default='None')
    
    def calculateAge(self):
        age = timezone.datetime.now().year - self.birthDate.year
        month = timezone.datetime.now().month - self.birthDate.month
        if month < 0:
            age = age - 1
        elif month == 0:
            day = timezone.datetime.now().day - self.birthDate.day
            if day < 0:
                age = age - 1
        return age

    def __str__(self):
        fullName = '%s %s' % (
            self.name,
            self.surname,
        )
        return fullName
    
    
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
    IdNumber = models.IntegerField()
    license = models.CharField(max_length=20)
    mail = models.EmailField()
    tel = models.IntegerField()
    address = models.TextField(blank=True)
    speciality = models.CharField(max_length=40)
    department = Department.name

    def __str__(self):
        fullName = '%s %s' % (
            self.name,
            self.surname,
        )
        return fullName
    
    
class History(models.Model):
    patient = models.OneToOneField(Patient, null=True, blank=True, on_delete=models.CASCADE)
    patientName = Patient.name
    doctor = Doctor.name
    numId = models.IntegerField()
    
    
class Registro(models.Model):
    date = models.DateField()
    timeIn = models.TimeField(null=True)
    timeOut = models.TimeField(null=True)
    diagnose = models.TextField(blank=True)
    comments = models.TextField(blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    history = models.OneToOneField(History, null=True, blank=True, on_delete=models.CASCADE) #la idea sería que los registros de un paciente se unifiquen en una hc
    
    def __str__(self):
        return self.comments
    
class Appointment(models.Model):
    date = models.DateField(auto_now_add=True, null=True)
    appointmentDate = models.DateField(null=True)
    time = models.TimeField(null=True)
    state = models.BooleanField()
    cause = models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return 'Programada - %s Dia - %s Hora - %s Paciente - %s Medico - %s' % (
            self.date,
            self.appointmentDate,
            self.time,
            self.patient,
            self.doctor,
        )
