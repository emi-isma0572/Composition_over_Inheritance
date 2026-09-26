from abc import ABC, abstractmethod

class Commission(ABC):
    @abstractmethod
    def get_commission(self) -> float:
        pass