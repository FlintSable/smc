""" Assignment One: Employee class - Nicholas Noochla-or
"""
from enum import Enum

class Employee:
    NAME = ('unidentified')
    EMPLOYEE_NUMBER = 999
    BENEFITS = True
    Shift = Enum("Shift", ["DAY", "SWING", "NIGHT"])
    SHIFT = Shift.DAY


    def __init__(self, nNAME=('unidentified'), eEMPLOYEE_NUMBER=999, sSHIFT="DAY"):
        self.NAME = nNAME
        self.EMPLOYEE_NUMBER = eEMPLOYEE_NUMBER
        self.BENEFITS = self.determine_benifits()
        self.SHIFT = sSHIFT

    def determine_benifits(Emp_Num):
        if(int(Emp_Num.EMPLOYEE_NUMBER) < 500):
            return True
        elif(int(Emp_Num.EMPLOYEE_NUMBER) >= 500):
            return False

    
    def to_string(self):
        return self.SHIFT.name # gets you just the name


    # mutator ("set") methods ------------------------------------------
    @property
    def employee_name(self):
        return self.NAME


    @property
    def employee_id(self):
        return self.EMPLOYEE_NUMBER
    

    @property
    def employee_shift(self):
        return self.SHIFT


    @employee_name.setter
    def employee_name(self, new_name):
        self.NAME = new_name
    

    @employee_id.setter
    def employee_id(self, new_num):
        self.EMPLOYEE_NUMBER = new_num
    

    @employee_shift.setter
    def employee_shift(self, new_shift):
        self.SHIFT = new_shift


class Shift(Enum):
    DAY = 1
    SWING = 2
    NIGHT = 3


    def __str__(self):
        ret_str = self.name[0].upper() + self.name[1:].lower()


def main():
    print("starting")
    employee_directory = []
    Emp_1 = Employee("Jam Juice", 100, Employee.Shift.DAY)
    # Emp_1 = Employee("Jam Juice", 100, Employee.Shift.DAY)
    # Emp_1 = Employee("Jam Juice", 100, Employee.Shift.DAY)

    employee_directory.append(Emp_1)
    print(employee_directory[0].NAME, Emp_1.EMPLOYEE_NUMBER, Emp_1.BENEFITS, Emp_1.SHIFT)
    Emp_1.employee_name = "Newbie"
    Emp_1.employee_id = "230"
    # Emp_1.employee_shift = Shift.NIGHT

    print(Emp_1.employee_name)
    print(Emp_1.employee_id)
    print(repr(Emp_1.employee_shift))
    print(type(Emp_1.employee_shift))
    print(Emp_1.to_string())

if __name__ == "__main__":
    main()

"""

"""