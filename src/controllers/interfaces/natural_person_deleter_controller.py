from abc import ABC, abstractmethod

class NaturalPersonDeleterControllerInterface(ABC):
    
    @abstractmethod
    def delete(self, name: str) -> None:
        pass
