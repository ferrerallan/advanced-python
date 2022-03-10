from pyexpat import model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import serializers
from django.db import models

from pep.models import  Patient, MedicalInsurance


#models


class MedicalInsuranceModelSerializer(serializers.ModelSerializer):
  name=serializers.CharField()

  class Meta:
    model=MedicalInsurance
    fields=['name']
  
class PatientModelSerializer(serializers.ModelSerializer):
  name = serializers.CharField()
  cpf = serializers.CharField()
  medicalInsurance = MedicalInsuranceModelSerializer(many=False)

  class Meta:
    model = Patient
    fields = ['name','cpf','medicalInsurance']

class PatientSimpleSerializer(serializers.Serializer):
  name = serializers.CharField()
  cpf = serializers.CharField()
 

class TestSerializersView(APIView):
  def get(self,request):
    print("testing serializers..")
    output="testing"
    patient = Patient()
    patient.medicalInsurance = MedicalInsurance()
    patient.name="Allan"
    patient.cpf="29840569813"
    patient.medicalInsurance.name="SUS"
    
    #a simpe serializers
    serialPatient = PatientSimpleSerializer(patient)
    print(serialPatient.data)

    #model serializer
    serialPatient2 = PatientModelSerializer(patient)
    print(serialPatient2.data)
    
    return Response(output)