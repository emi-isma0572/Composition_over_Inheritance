from typing import Optional
from contract import Contract
from commission import Commission

class Employee:
    def __init__(self, name: str, id: int, contract: Contract, commission: Optional[Commission] = None):
        self.name = name
        self.id = id
        self.contract = contract
        self.commission = commission

    def compute_pay(self) -> float:
        total = self.contract.get_base_pay()
        if self.commission is not None:
            total += self.commission.get_commission()
        return total

    def __str__(self) -> str:
        return f"[{self.id}] {self.name} - Pay: ${self.compute_pay():,.2f}"