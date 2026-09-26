from contract import Contract

class FreelancerContract(Contract):
    def __init__(self, project_fee: float):
        self.project_fee = project_fee

    def get_base_pay(self) -> float:
        return self.project_fee