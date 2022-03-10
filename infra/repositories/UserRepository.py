from usuarios.models import *

from application.usecases.createuser.protocols.AbsCreateUserRepository import AbsCreateUserRepository
class UserRepository(AbsCreateUserRepository):
  def create(self, userEntity):
    newUser = Usuario()
    newUser.name = userEntity.name
    newUser.cpf = userEntity.cpf

    newUser.save()

    userEntity.id = newUser.id

    return userEntity