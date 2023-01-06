class Company:
    register = {}

    def __init__(self, company, employee):
        self.company = company
        self.employee = employee

    def add_employee(self):
        if self.company not in Company.register:
            Company.register[self.company] = []
        if self.employee not in Company.register[self.company]:
            Company.register[self.company].append(self.employee)

    def print_func(self):
        for company in Company.register.keys():
            print(company)
            for employees in Company.register[company]:
                print(f"-- {employees}")


command = input()
while command != 'End':
    company_name, employee_id = command.split(' -> ')
    object = Company(company_name, employee_id)
    object.add_employee()
    command = input()

object.print_func()