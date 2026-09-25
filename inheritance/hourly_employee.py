from employee import Employee

class HourlyEmployee(Employee):
    def __init__(self, name: str, id: int, hourly_rate: float, hours_worked: float):
        super().__init__(name, id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def compute_pay(self) -> float:
        return self.hourly_rate * self.hours_worked