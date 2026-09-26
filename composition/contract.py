from abc import ABC, abstractmethod

class Contract(ABC):
    @abstractmethod
    def get_base_pay(self) -> float:
        pass