class CreateUser:
  createUserRepository=None
  def __init__(self,createUserRepository,integrateLegacyUser):
    self.createUserRepository = createUserRepository
    self.integrateLegacyUser = integrateLegacyUser

  def create(self, createRepositoryDTO):
    newUser = createRepositoryDTO.toEntity()
    if (not newUser.isValid()):
      return "user is invalid"  
    
    try:
      self.createUserRepository.create(newUser)
      self.integrateLegacyUser.integrate(newUser)
    except:
      #rollback all features..
      None

    return ""
    