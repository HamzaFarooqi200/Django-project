from django.db import models
from django.core.exceptions import ValidationError


def check_phone_number(number):
    if len(number) != 11:
        raise ValidationError("the number should be 11 digit")
    elif number[:2] != "03":
        raise ValidationError("number must start with 03!!!")

class Doctor(models.Model):
    name = models.CharField(max_length=10)
    specialization = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=11, validators=[check_phone_number])

    def __str__(self) -> str:
        return str(self.name)

class Nurse(models.Model):
    name = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=11, validators=[check_phone_number])

    def __str__(self) -> str:
        return str(self.name)

class Patient(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    doctor = models.ManyToManyField(Doctor, related_name='doctors')
    nurse = models.ForeignKey(Nurse, on_delete= models.CASCADE, related_name='nurses')
    date_admitted = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)
    
class Hospital(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='hospitalpatients')
    doctor = models.ManyToManyField(Doctor)
    nurse = models.ForeignKey(Nurse, on_delete= models.CASCADE)

    def __str__(self) -> str:
        return str(self.patient)
    

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patientsrecords')
    diagonses = models.TextField()
    prescription = models.TextField()

    def __str__(self) -> str:
        return str(self.patient)