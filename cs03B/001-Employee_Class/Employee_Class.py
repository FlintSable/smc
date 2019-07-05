""" Assignment One: Employee class - Nicholas Noochla-or
"""
from enum import Enum

class Employee:


    NAME = ('unidentified')
    EMPLOYEE_NUMBER = 999
    BENEFITS = True
    SHIFT = Enum("Shift", ["DAY", "SWING", "NIGHT"])

    def __init__(self, nNAME=('unidentified'), eEMPLOYEE_NUMBER=999, sSHIFT="DAY"):
        self.NAME = nNAME
        self.EMPLOYEE_NUMBER = eEMPLOYEE_NUMBER
        self.BENEFITS = self.determine_benifits()
        self.SHIFT = sSHIFT

    # def get_shift(self):
    #     return self.SHIFT.value

    def determine_benifits(Emp_Num):
        print(Emp_Num.EMPLOYEE_NUMBER)
        if(int(Emp_Num.EMPLOYEE_NUMBER) < 500):
            return True
        elif(int(Emp_Num.EMPLOYEE_NUMBER) >= 500):
            return False

  
class Shift(Enum):
    DAY = 1
    SWING = 2
    NIGHT = 3
    def __str__(self):
        ret_str = self.name[0].upper() + self.name[1:].lower()


def main():
    print("starting")
    Emp_1 = Employee("Jam Juice", 100, "SWING")
    print(Emp_1.NAME, Emp_1.EMPLOYEE_NUMBER, Emp_1.BENEFITS, Emp_1.SHIFT)
    Emp_1.SHIFT = "NIGHT"
    # print(Emp_1.get_shift())



if __name__ == "__main__":
    main()

"""

"""