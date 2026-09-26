from contract import Contract

class SalariedContract(Contract):
    def __init__(self, monthly_salary: float):
        self.monthly_salary = monthly_salary

    def get_base_pay(self) -> float:
        return self.monthly_salary