from commission import Commission

class ContractCommission(Commission):
    def __init__(self, amount: float):
        self.amount = amount

    def get_commission(self) -> float:
        return self.amount