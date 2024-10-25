from abc import ABC, abstractmethod

class LegalEntityDeleterControllerInterface(ABC):

    @abstractmethod
    def delete(self, name: str) -> None:
        pass
