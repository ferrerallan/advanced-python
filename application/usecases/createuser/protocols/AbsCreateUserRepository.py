from abc import ABCMeta, abstractmethod

class AbsCreateUserRepository(metaclass=ABCMeta):
  @abstractmethod
  def create(self,user):
    pass