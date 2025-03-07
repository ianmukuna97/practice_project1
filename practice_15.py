# dates
# inheritance
# error handling

class Employee:
    def __init__(self, name, id_no , dob, gender):
        self.name = name
        self.id_number = id_no
        self.dob = dob
        self.gender = gender

    def show_details(self):
        print(f"Name: {self.name}\nID: {self.id_number}\nDOB: {self.dob}\nGender: {self.gender}")

class PermanentEmployee(Employee):
    def __init__(self, name, id_no, dob, gender, salary):
        super().__init__(name, id_no, dob, gender)
        self.salary = salary

    def print_salary(self):
        print(f"Salary is ${self.salary}")

      # override
    def print_details(self):
        super().show_details()
        print(f"Salary is ${self.salary}")
        
class TemporaryEmployee(Employee):
    def __init__(self, name, id_no, dob, gender, hourly_pay, end_date):
        super().__init__(name, id_no, dob, gender)
        self.hourly_pay = hourly_pay
        self.end_date = end_date

    def print_hourly_pay(self):
        print(f"Hours pay is : ${self.hourly_pay}")

    def print_end_date(self):
        print(f"End date is: ${self.end_date}")

p1 = PermanentEmployee("George James", "22334455", "7-05-1995","M", 10000)
p1.show_details()
p1.print_salary()
print("--------------------------")
t1 = TemporaryEmployee("Sasha Said", "55544477", "4-7-1997", "F", 2000, "4-5-2024")
t1.show_details()
t1.print_end_date()
t1.print_hourly_pay()
