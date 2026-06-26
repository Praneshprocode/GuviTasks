#Employee management Task

class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        pass

class RegularEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class Manager(Employee):
    def __init__(self, name, monthly_salary, bonus):
        super().__init__(name)
        self.monthly_salary = monthly_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.monthly_salary + self.bonus

employees = [
    RegularEmployee("Goku", 70000),
    ContractEmployee("Broly", 500, 100),
    Manager("Krilen", 75000, 15000)
]

print(" Employee Salaries ")
for emp in employees:
    print(f"{emp.name}: {emp.calculate_salary()}")