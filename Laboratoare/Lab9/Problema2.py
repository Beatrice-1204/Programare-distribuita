class Employee:
    def __init__(self, name, salary):
        self.name = str(name)
        self.salary = float(salary)

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary:g}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # apelează constructorul clasei părinte
        self.department = str(department)

    def get_details(self):
        return f"Manager: {self.name}, Salary: {self.salary:g}, Department: {self.department}"


# Exemplu de utilizare (fără valori prestabilite)
name_emp = input("Nume angajat: ")
salary_emp = float(input("Salariu angajat: "))
emp = Employee(name_emp, salary_emp)

name_mgr = input("Nume manager: ")
salary_mgr = float(input("Salariu manager: "))
dept_mgr = input("Departament manager: ")
mgr = Manager(name_mgr, salary_mgr, dept_mgr)

print(emp.get_details())
print(mgr.get_details())
