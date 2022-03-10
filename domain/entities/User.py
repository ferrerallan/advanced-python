from domain.entities.protocols.AbstractEntity import AbstractEntity

class User(AbstractEntity):
  id=None
  name=""
  cpf=""
  errors=""

  def __init__(self):
    pass
  
  def isValid(self):
    if (self.name==""):
      self.errors+= "name is required"
    return self.errors==""

  def getErrors(self):
      return self.errors