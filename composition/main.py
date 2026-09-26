from employee import Employee
from hourly_contract import HourlyContract
from salaried_contract import SalariedContract
from freelancer_contract import FreelancerContract
from contract_comission import ContractCommission

def main():
    employees = [
        Employee("Emilio Renteria", 101, HourlyContract(hourly_rate=25.0, hours_worked=160)),
        Employee("Suemi Villanueva", 102, HourlyContract(hourly_rate=25.0, hours_worked=160), ContractCommission(500.0)),
        Employee("Maria Fernanda", 201, SalariedContract(monthly_salary=4500.0)),
        Employee("Emanuel Aldana", 202, SalariedContract(monthly_salary=4500.0), ContractCommission(1200.0)),
        Employee("Robin Gonzalez", 301, FreelancerContract(project_fee=1800.0)),
        Employee("Sofia Vargas", 302, FreelancerContract(project_fee=1800.0), ContractCommission(350.0)),
    ]

    print("Payroll Demonstration (Composition):")
    for emp in employees:
        print(emp)

if __name__ == "__main__":
    main()