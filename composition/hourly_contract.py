from contract import Contract

class HourlyContract(Contract):
    def __init__(self, hourly_rate: float, hours_worked: float):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def get_base_pay(self) -> float:
        return self.hourly_rate * self.hours_worked