class Factory:
    working = 'False'
    Name = 'ND'
    Employees = []
    Id = 1

    def __init__(self, name=Name):
        super(Factory, self).__init__()
        self.Name = name
        print(f'Factory \"{name}\" is created')

    def open(self):
        self.working = True
        print('Factory is opened')

    def close(self):
        self.working = False
        print('Factory is closed')

    def add_employee(self, name):
        new_worker = Employee(name, self.Id)
        self.Id += 1
        self.Employees.append(new_worker)

    def print_employees(self):
        for man in self.Employees:
            print(f'{man.Name}, {man.Id}')


class Employee:
    Name = 'ND'
    Id = 'ND'

    def __init__(self, name=Name, employee_id=Id):
        super(Employee, self).__init__()
        self.Name = name
        self.Id = employee_id


factory = Factory('Yep')
print(factory.Name)

factory.add_employee('John')
factory.add_employee('Ben')

factory.print_employees()
