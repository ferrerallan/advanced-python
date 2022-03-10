from domain.entities.User import User

class CreateUserDTO:
  def __init__(self, name, cpf):
    self.name = name
    self.cpf = cpf
  
  def toEntity(self):
    newUser = User()
    newUser.name = self.name
    newUser.cpf = self.cpf
    
    return newUser