class Person:
    def __init__(self, firstname, lastname, age, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"firstname={self.firstname}, lastname={self.lastname}, age={self.age}, gender={self.gender}"


class Employee(Person):
    def __init__(self, firstname, lastname, age, gender, department):
        super().__init__(firstname, lastname, age, gender)
        self.department = department

    def __str__(self):
        return super().__str__() + f", department={self.department}"


class Manager(Employee):
    def __init__(self, firstname, lastname, age, gender, department):
        super().__init__(firstname, lastname, age, gender, department)

    def __str__(self):
        return super().__str__() + f""


class Company:
    def __init__(self, name, employees=None, departments=None, managers=None):
        self.name = name
        if employees is None:
            self.employees = []
        if departments is None:
            self.departments = []
        if managers is None:
            self.managers = []

    def add_employee(self, employee_to_add):
        if type(employee_to_add) is Employee:
            if employee_to_add.department in self.departments:
                self.employees.append(employee_to_add)
            else:
                print(f'\nAdding Employee unsuccessful. Department \'{employee_to_add.department}\' doesn\'t exist')
                print(f'If this wasn\'t a typo, add the department first and then try again\n')
        else:
            print(f'\nEmployee to add is not of type Employee\n')

    def create_employee(self, firstname, lastname, age, gender, department):
        self.add_employee(Employee(firstname, lastname, age, gender, department))

    def remove_employee(self, employee_to_remove):
        self.employees.remove(employee_to_remove)

    def add_manager(self, manager_to_add):
        if type(manager_to_add) is Manager:
            if manager_to_add.department in self.departments:
                managers_deps = [d.department for d in self.managers]
                if manager_to_add.department not in managers_deps:
                    self.managers.append(manager_to_add)
                else:
                    print(f'\nAdding Manager unsuccessful. Department \'{manager_to_add.department}\' already has a manager\n')
            else:
                print(f'\nAdding Manager unsuccessful. Department \'{manager_to_add.department}\' doesn\'t exist')
                print(f'If this wasn\'t a typo, add the department first and then try again\n')
        else:
            print(f'\nManager to add is not of type Manager\n')

    def create_manager(self, firstname, lastname, age, gender, department):
        self.add_manager(Manager(firstname, lastname, age, gender, department))

    def remove_manager(self, manager_to_remove):
        self.managers.remove(manager_to_remove)

    def add_department(self, department_to_add):
        self.departments.append(department_to_add)

    def remove_department(self, department_to_remove):
        if department_to_remove not in self.departments:
            print(f'\nDepartment {department_to_remove} doesn\'t exist\n')
            return

        current_deps = [d.department for d in self.employees]

        if department_to_remove not in current_deps:
            self.departments.remove(department_to_remove)
            return
        print(f'\nDepartment \'{department_to_remove}\' has employees assigned to it.')
        print(f'First remove all employees if you wan\'t to remove the department\n')

    def show_employees(self):
        print(f'\nThere are {len(self.employees)} employees:')
        for i, v in enumerate(self.employees):
            print(f'{i + 1}: {v.lastname}, {v.firstname}')

    def show_departments(self):
        print(f'\nThere are {len(self.departments)} departments:')
        for i, v in enumerate(self.departments):
            print(f'{i + 1}: {v}')

    def show_managers(self):
        print(f'\nThere are {len(self.managers)} managers:')
        for i, v in enumerate(self.managers):
            print(f'{i + 1}: {v.lastname}, {v.firstname} - {v.department}')

    def employees_per_department(self):
        count = {v: 0 for v in self.departments}

        for e in self.employees:
            count[e.department] += 1

        print(f'Employees per department:')
        for c in count:
            print(f'{c}: {count[c]}')


    def gender_division(self):
        count = {'male': 0, 'female': 0}
        for e in self.employees:
            count[e.gender] += 1

        print(f'{count["male"]} / {count["female"]} = {count["male"] / count["female"] * 100}%')



if __name__ == '__main__':
    p1 = Person('John', 'Doe', 25, 'male')
    e1 = Employee('Jane', 'Doe', 20, 'female', 'r&d')
    e2 = Employee('Christian', 'Sheppard', 29, 'male', 'finance')
    m1 = Manager('Msax', 'Musterman', 30, 'male', 'production')

    company = Company('My Company')

    company.add_department('r&d')
    company.add_employee(e1)

    company.add_department('finance')
    company.add_employee(e2)

    company.add_department('production')
    company.add_manager(m1)

    company.create_employee('Jeremy', 'Birmingham', 50, 'male', 'production')

    company.create_manager('Tom', 'Tom', 35, 'male', 'finance')

    company.show_managers()
    company.show_employees()
    company.show_departments()
