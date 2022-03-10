from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse

class HomeView(APIView):
  def get(self,request, id):
    print("passou")
    output = f"id is {id}"
    return Response(output, status=status.HTTP_201_CREATED)
  
