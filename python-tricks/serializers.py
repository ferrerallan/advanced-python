from rest_framework import serializers
from django.db import models

from advancedproject import settings

#models
class MedicalInsurance(models.Model):
  name=models.CharField()

class Patient(models.Model):
  name=models.CharField()
  cpf=models.CharField()
  insurance=models.ForeignKey(MedicalInsurance, on_delete=models.PROTECT,null=True)

class PatientSimpleSerializer(serializers.Serializer):
  name = serializers.CharField()
  cpf = serializers.CharField()
  insurance = serializers.ModelField()

#simple serializer
patient = Patient()
patient.name="Allan"
patient.cpf=29840569813
patient.insurance = MedicalInsurance()
patient.insurance.name="SUS"


serialPatient = PatientSimpleSerializer(patient)
print(serialPatient.data)