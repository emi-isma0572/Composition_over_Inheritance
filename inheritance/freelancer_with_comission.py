from freelancer import Freelancer

class FreelancerWithCommission(Freelancer):
    def __init__(self, name: str, id: int, project_fee: float, commission: float):
        super().__init__(name, id, project_fee)
        self.commission = commission

    def compute_pay(self) -> float:
        return super().compute_pay() + self.commission