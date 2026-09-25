from employee import Employee

class Freelancer(Employee):
    def __init__(self, name: str, id: int, project_fee: float):
        super().__init__(name, id)
        self.project_fee = project_fee

    def compute_pay(self) -> float:
        return self.project_fee