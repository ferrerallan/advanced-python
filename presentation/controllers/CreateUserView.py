from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from application.usecases.createuser.protocols.CreateUserDTO import CreateUserDTO
from application.usecases.createuser.CreateUser import CreateUser
from infra.repositories.UserRepository import UserRepository
from infra.services.IntegrateLegacyUserSAP import IntegrateLegacyUserSAP

class CreateUserView(APIView):
  permission_classes = (IsAuthenticated,)
  def post(self,request):
    #validate request
    errors=""
    requiredFields=["name","cpf"]
    for field in requiredFields:
      if field not in request.data:
        errors+=f"{field} is required"
   
    createUserDTO = CreateUserDTO(request.data["name"], request.data["cpf"])

    if errors != "":
      return Response(errors, status=status.HTTP_400_BAD_REQUEST)
    
    createUser = CreateUser(UserRepository(),IntegrateLegacyUserSAP() )
    result = createUser.create(createUserDTO)
    
    if result != "":
      return Response(result, status=status.HTTP_400_BAD_REQUEST)
    
    return Response("success", status=status.HTTP_201_CREATED)

  def get(self,request, id):
    output = f"id is {id}"
    return Response(output, status=status.HTTP_201_CREATED)
  
