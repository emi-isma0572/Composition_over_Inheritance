from hourly_employee import HourlyEmployee

class HourlyEmployeeWithCommission(HourlyEmployee):
    def __init__(self, name: str, id: int, hourly_rate: float, hours_worked: float, commission: float):
        super().__init__(name, id, hourly_rate, hours_worked)
        self.commission = commission

    def compute_pay(self) -> float:
        return super().compute_pay() + self.commission