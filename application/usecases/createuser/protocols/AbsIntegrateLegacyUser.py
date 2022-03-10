from abc import ABCMeta, abstractmethod
 
class AbsIntegrateLegacyUser(metaclass=ABCMeta):
# contratos, acordos...
  @abstractmethod
  def integrate(self, user):
    pass
    
