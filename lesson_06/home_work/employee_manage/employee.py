from lesson_06.home_work.employee_manage.main_person import MainPerson


class Employee(MainPerson):
    def __init__(self, name, salary,role):
        super().__init__(name)  # Call the parent class's initializer
        self.salary = salary
        self.role = role

#salary getter
    @property
    def salary(self):
        return self._salary

#salary setter
    @salary.setter
    def salary(self, new_salary: float):

        if new_salary >= 0:
            self._salary = new_salary

        else:
            raise ValueError("Salary must be a positive number")

    # role getter :
    @property
    def role(self):
        return self._role

#role setter
    @role.setter
    def role(self, new_role: str):
        if len(new_role) > 0:
            self._role = new_role
        else:
            raise ValueError("role cannot be empty ")


try_usage = Employee(input("Enter employee name"),int(input("Enter employee salary")),input("enter employee role"))
print(f"Employee name:{try_usage.get_name}\n Employee salary: {try_usage.salary} \n Employee role: {try_usage.role}")

try:
    try_usage = Employee("Mir", -88, "")  # This should trigger the setter and raise an error
    print(try_usage.get_name, try_usage.salary, try_usage.role)
except ValueError as e:
    print(e)

try:
    try_usage = Employee("Mir", 88, "")  # This should trigger the setter and raise an error
    print(try_usage.get_name, try_usage.salary, try_usage.role)
except ValueError as e:
     print(e)