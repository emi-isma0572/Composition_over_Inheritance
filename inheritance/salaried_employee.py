from employee import Employee

class SalariedEmployee(Employee):
    def __init__(self, name: str, id: int, monthly_salary: float):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def compute_pay(self) -> float:
        return self.monthly_salary