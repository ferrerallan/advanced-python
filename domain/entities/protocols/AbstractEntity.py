from abc import ABCMeta, abstractmethod
 
class AbstractEntity(metaclass=ABCMeta):
    # contratos, acordos...
    @abstractmethod
    def isValid(self):
        pass
    @abstractmethod
    def getErrors(self):
        pass
