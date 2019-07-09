""" Assignment Two: Sorted employees - Nicholas Noochla-or
"""
from enum import Enum
from queue import Queue
import random
import re

def main():
    employee_directory = []
    sudo_usernames_data = [
        "Inger Hella", 
        "Saga Janina",
        "Alfred Dorotea",
        "Tessan Helen",
        "Michael Rigmor",
        "Edith Ida",
        "John Henrike",
        "Hella Lukas",
        "Thyra Karolina",
        "Øyvind Nathalie",
        "Miroslav Tikhon",
        "Tòmas Prokhor",
        "Timofei Vitaliy",
        "Beileag Logan",
        "Filipp Vadim",
        "Ruaridh Lilia",
        "Filat Svyatoslav",
        "Sofiya Bhaltair",
        "Max Saveli",
        "Yeva Snezhana"
    ]

    for i, val in enumerate(sudo_usernames_data):
        # output = f'{i} {val} {random.randrange(100,999)} {predict_shift[random.randrange(1,4)]}'
        employee_directory.append(Employee(val, random.randrange(100, 999), random.randrange(1,4)))
        # print(employee_directory[i].to_string())
    print("Before id number sort: \n ----------")
    EmployeeArrayUtilities.print_array(employee_directory)

    array_size = len(employee_directory)
    EmployeeArrayUtilities.print_array(employee_directory, "\nBefore last-name sort:")
    EmployeeArrayUtilities.sort_array(employee_directory, array_size)
    EmployeeArrayUtilities.print_array(employee_directory, "\nAfter last-name sort: ")

    s1 = Queue(10, Employee())
    print("capacity: ", s1.get_capacity())
    # print(employee_directory[0])
    s1.add(employee_directory[0])
    s1.add(employee_directory[1])
    s1.add(employee_directory[2])
    s1.add(employee_directory[3])
    s1.add(employee_directory[4])

    print(s1.que)

    for k in range(0, 5):
        print("[" + str(s1.remove()) + "]")


    # emp_1 = Employee()
    # emp_2 = Employee("Tom Jones", 374, 1)
    # emp_3 = Employee("Tim Smith", 99877, 1)
    # employee_directory.extend([emp_1, emp_2, emp_3])
    # print(employee_directory[0].to_string())
    # print(employee_directory[1].to_string())
    # print(employee_directory[2].to_string())
    # print("New user creation: \n")
    # print("Enter First and Lastname: ", end="")
    # f_name = input()
    # print("Enter id number: ", end="")
    # new_id = input()
    # validate_number(new_id)
    
    # print("1 - DAY\n2 - SWING\n3 - NIGHT\n")
    # print("Enter number to enter shift information: ", end="")
    # new_shift = input()
    # emp_4 = Employee(f_name, int(new_id), int(new_shift))
    # employee_directory.append(emp_4)
    # print(employee_directory[3].to_string())


def validate(data_name, data_number, data_shift):
    if(data_number < 100 or data_number > 999):
        return False
    elif(data_shift == 1):
        return True
    elif(data_shift == 2):
        return True
    elif(data_shift == 3):
        return True       
    else:
        return False



def validate_number(data_number):
    try:
        s = data_number
        s.isdigit()
        if(re.search('[a-zA-Z]', s)):
            print('err')
            raise EmpNumError
        output = int(s)
        if(output < 100):
            print('err')

            raise EmpNumError
        elif(output > 999):
            print('err')

            raise EmpNumError
        return output
    except:
        pass
        
class EmployeeArrayUtilities:
    @staticmethod
    def print_array(employee_array, optional_title="--- The Employees -----------:\n"):
        print(optional_title)
        for i, val in enumerate(employee_array):
            print(val.to_string())


    @classmethod
    def sort_array(cls, data, array_size):
        for k in range(array_size):
            if not cls.float_largest_to_top(data, array_size - k):
                return

    
    @staticmethod
    def float_largest_to_top(data, array_size):
        changed = False
        for k in range(array_size - 1):
            if Employee.compare_two_employees(data[k], data[k + 1]) > 0:
                data[k], data[k+1] = data[k+1], data[k]
                changed = True
        return changed


class EmpNumError(Exception):
    """Value is less than 100 or greater then 999"""
    pass

class Employee:
    NAME = ('unidentified')
    EMPLOYEE_NUMBER = 999
    
    Shift = Enum("Shift", ["DAY", "SWING", "NIGHT"])
    SHIFT = Shift.DAY


    def __init__(self, nNAME=('unidentified'), eEMPLOYEE_NUMBER=999, sSHIFT=Shift.DAY):
        if(nNAME==('unidentified') and eEMPLOYEE_NUMBER==999):
            self.NAME = nNAME
            self.EMPLOYEE_NUMBER = eEMPLOYEE_NUMBER
            self.BENEFITS = self.determine_benifits()
            if(sSHIFT == 1):
                self.SHIFT = Shift.DAY
            elif(sSHIFT == 2):
                self.SHIFT = Shift.SWING
            elif(sSHIFT == 3):
                self.SHIFT = Shift.NIGHT
        elif(validate(nNAME, eEMPLOYEE_NUMBER, sSHIFT)):
            self.NAME = nNAME
            self.EMPLOYEE_NUMBER = eEMPLOYEE_NUMBER
            self.BENEFITS = self.determine_benifits()
            if(sSHIFT == 1):
                self.SHIFT = Shift.DAY
            elif(sSHIFT == 2):
                self.SHIFT = Shift.SWING
            elif(sSHIFT == 3):
                self.SHIFT = Shift.NIGHT
        else:
            self.BENEFITS = self.determine_benifits()
            print("a parameter given was incorrect\na default object will be created\n")


    def determine_benifits(Emp_Num):
        if(int(Emp_Num.EMPLOYEE_NUMBER) < 500):
            return True
        elif(int(Emp_Num.EMPLOYEE_NUMBER) >= 500):
            return False


    def to_string(self):
        employee_details = (f'{self.NAME} #{self.EMPLOYEE_NUMBER} '
                            f'({"Benifits" if self.BENEFITS else "No benefits"})'
                            f'\nShift: {self.SHIFT.name} \n ----------'
                            )
        return employee_details


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

    # static/class methods -----------------------------------
    @classmethod
    def compare_two_employees(cls, first_employee, second_employee):
        """ comparison done on parameters' last names """
        return cls.compare_numbers(first_employee.employee_id, second_employee.employee_id)

    @staticmethod
    def compare_numbers(num1, num2):
        """ returns -1 if first < second
           +1 if first > second, and 0 if same """
        if num1 < num2:
            return -1
        if num1 > num2:
            return 1
        return 0

class Shift(Enum):
    DAY = 1
    SWING = 2
    NIGHT = 3

    def __str__(self):
        ret_str = self.name[0].upper() + self.name[1:].lower()
        return ret_str


if __name__ == "__main__":
    main()

"""

"""