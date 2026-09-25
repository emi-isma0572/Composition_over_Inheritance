from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    @abstractmethod
    def compute_pay(self) -> float:
        pass

    def __str__(self) -> str:
        return f"[{self.id}] {self.name} - Pay: ${self.compute_pay():,.2f}"