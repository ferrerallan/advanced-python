from django.db import models

# Create your models here.

class MedicalInsurance(models.Model):
  name=models.CharField(max_length=200)

class Patient(models.Model):
  name=models.CharField(max_length=200)
  cpf=models.CharField(max_length=11)
  medicalInsurance=models.ForeignKey(MedicalInsurance,on_delete=models.PROTECT, null=True)
  