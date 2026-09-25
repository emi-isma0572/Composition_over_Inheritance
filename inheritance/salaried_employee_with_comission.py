from salaried_employee import SalariedEmployee

class SalariedEmployeeWithCommission(SalariedEmployee):
    def __init__(self, name: str, id: int, monthly_salary: float, commission: float):
        super().__init__(name, id, monthly_salary)
        self.commission = commission

    def compute_pay(self) -> float:
        return super().compute_pay() + self.commission