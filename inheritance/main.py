from hourly_employee import HourlyEmployee
from salaried_employee import SalariedEmployee
from freelancer import Freelancer
from hourly_employee_with_comission import HourlyEmployeeWithCommission
from salaried_employee_with_comission import SalariedEmployeeWithCommission
from freelancer_with_comission import FreelancerWithCommission

def main():
    employees = [
        HourlyEmployee("Emilio Renteria", 101, hourly_rate=25.0, hours_worked=160),
        HourlyEmployeeWithCommission("Suemi Villanueva", 102, hourly_rate=25.0, hours_worked=160, commission=500.0),
        SalariedEmployee("Maria Fernanda", 201, monthly_salary=4500.0),
        SalariedEmployeeWithCommission("Emanuel Aldana", 202, monthly_salary=4500.0, commission=1200.0),
        Freelancer("Robin Gonzalez", 301, project_fee=1800.0),
        FreelancerWithCommission("Sofia Vargas", 302, project_fee=1800.0, commission=350.0),
    ]

    print("Payroll Demonstration (Inheritance):")
    for emp in employees:
        print(emp)

if __name__ == "__main__":
    main()