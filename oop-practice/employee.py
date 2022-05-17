class Employee:

    raise_amount = 2.5
    number_of_employee =0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.number_of_employee+=1

    def email(self):
        return self.first + '.'+self.last + '@brainsation-23.com'
    def fullname(self):
         return self.first + ' ' + self.last

    def raise_salary(self):
        self.pay= int(self.pay*Employee.raise_amount)

    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==4:
            return False
        return  True



import datetime
today = datetime.date(2022,5,6)

print(Employee.is_workday(today))

emp1_str = 'rohit-hasan-3500'
first,last,pay = emp1_str.split('-')
em3 = Employee(first, last, int(pay))

print(em3.fullname())

emp1 = Employee("tahir","hasan",5300)
emp2 = Employee("Fazle","rabbi",4500)

print(Employee.number_of_employee)
emp1.raise_salary()
print(emp1.pay)
print(emp1.first + "."+ emp1.last +"@gmail.com")
print(emp1.email())

class developer(Employee):
    pass


