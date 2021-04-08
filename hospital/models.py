from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    pass
    # name = models.CharField(max_length=50)
    # email = models.EmailField(unique=True)
    # password = models.CharField(max_length=16)
    gender = models.CharField(max_length=10)
    #phonenumber = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    #birthdate = models.DateField(max_length=100)
    bloodgroup = models.CharField(max_length=5)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_receptionist = models.BooleanField(default=False)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    gender = models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    # birthdate = models.DateField(max_length=100)
    bloodgroup = models.CharField(max_length=5)
    user.is_patient = True
    def __str__(self):
        return self.name



doctor_choices = [('Dr.James', 'Dr.James'),
                  ('Dr.Tom', 'Dr.Tom'),
                  ('3PM-5PM', '3pm-5pm'),
                  ('5PM-7PM', '5pm-7pm'),
                  ('7PM-9PM', '7pm-9pm'), ]
email_choices = [('test@gmail.com', 'test@gmail.com'),
                  ('test@gmail.com', 'test@gmail.com'),
                 ]

class Appointment(models.Model):
    doctorname = models.CharField(max_length=50, choices=doctor_choices)
    doctoremail = models.EmailField(max_length=50, choices=email_choices)
    patientname = models.CharField(max_length=50)
    patientemail = models.EmailField(max_length=50)
    appointmentdate = models.DateField(max_length=10)
    appointmenttime = models.TimeField(max_length=10)
    symptoms = models.CharField(max_length=100)
    prescription = models.CharField(max_length=200)
    prescription = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )


    def __str__(self):
        return self.patientname + " you have appointment with " + self.doctorname

    def __str__(self):
        return self.patientname + " you have appointment with " + self.doctorname


class Receptionist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
    gender = models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    # birthdate = models.DateField(max_length=100)
    bloodgroup = models.CharField(max_length=5)

    def __str__(self):
        return self.name
