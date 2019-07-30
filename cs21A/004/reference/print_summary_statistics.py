""" Assignment Eleven: Table with Temperature Data - Nicholas Noochla-or
"""
import math
from functools import reduce

def print_header():
    """
    STEM Center Temperature Project
    Nicholas Noochla-or
    """
    print(f"\nSTEM Center Temperature Project \nNicholas Noochla-or")


def print_menu():
    """
    :param
    :return
    :print:
        Main Menu
        ---------
        1 - Process a new data file
        2 - Choose units
        3 - Edit room filter
        4 - Show summary statistics
        5 - Show temperature by date and time
        6 - Show histogram of temperatures
        7 - Quit

        What is your choice?
    """
    output = (
        "\n\nMain Menu\n" +
        "---------\n" +
        "1 - Process a new data file\n" +
        "2 - Choose units\n" +
        "3 - Edit room filter\n" +
        "4 - Show summary statistics\n" +
        "5 - Show temperature by date and time\n" +
        "6 - Show histogram of temperatures\n" +
        "7 - Quit\n\n" )
    for i in range(len(output)):
        print(output[i], end = "")
    pass


def convert_units(celsius_value, units):
    """
    :param
        celsius_value:
            integer or floating point number in celsius
        units:
            - units = 0, return temperature in Celsius (no change)
            - units = 1, return temperature in Fahrenheit
            - units = 2, return temperature in Kelvin
    :return:
        the celsius value returned as Celsius, Fahrenheit or Kelvin
    """
    output = 0.0
    if(units == 0):
        output = celsius_value
    elif(units == 1):
        output = celsius_value * (9/5) + 32
    elif(units == 2):
        output = celsius_value + 273.15
    else:
        return None
    return output


def recursive_sort(s, key=0):
    """
    :param
        s:
            list to sort
        key:
            - key = 0, refers to first value in tuple
            - key = 1, refers to second value in tuple
    :return:
        recursive call to recursive_sort function
        bubble sorted list
    """
    slist = s[:]
    if(key == 0):
        for i, (t1, t2, t3) in enumerate(slist): 
            try: 
                if slist[i+1][0] < t1:
                    (slist[i], slist[i+1]) = (slist[i+1],(t1,t2,t3))
                    return recursive_sort(slist)
            except IndexError: 
                pass
        return slist
    elif(key == 1):
        for i, (t1, t2, t3) in enumerate(slist): 
            try: 
                if slist[i+1][1] < t2:
                    (slist[i], slist[i+1]) = (slist[i+1],(t1,t2,t3)) 
                    return recursive_sort(slist, 1)
            except IndexError: 
                pass
        return slist


def print_filter(sensor_list, active_sensors):
    """
    4201: Foundations Lab [ACTIVE]
    4204: CS Lab [ACTIVE]
    4205: Tiled Room [ACTIVE]
    4213: STEM Center [ACTIVE]
    4218: Workshop Room [ACTIVE]
    Out: Outside [ACTIVE]

    :param
        sensor_list:
            list of tuples (srt, srt, int)
        active_sensors:
            list of integers
    :return:
        void
    """
    print("\n")
    for i, (t1, t2, t3) in enumerate(sensor_list):
        if(t3 in active_sensors):
            print(f'{t1}: {t2} [ACTIVE]')
        else:
            print(f'{t1}: {t2}')


def new_file(dataset):
    try:
        print("Please enter the filename of the new dataset:", end=" ")
        filename = input()
        test_file = open(filename, 'r')
        test_file.close()
        dataset.process_file(filename)
        print(f"Loaded {dataset.get_loaded_temps()} samples")
        print("Please provide a 3 to 20 character name for the dataset", end=" ")
        data_name = input()
        dataset.name = data_name
        return True
    except FileNotFoundError:
        print("File not found, could not open file")
        return False
        

def choose_units(current_unit, unit_options):
    print(current_unit)
    new_choice = int()
    print("Current units in", unit_options[current_unit][0])
    print("Choose new units:")
    for i in unit_options:
        print(f"{i} - {unit_options[i][0]}")
    print("Which unit?")
    new_choice = input()
    if new_choice in (str(unit_options.keys())):
        new_choice = int(new_choice)
    while new_choice not in(list(unit_options.keys())):
        try:
            new_choice = int(new_choice)
            print("Choose new units:")
        except ValueError:
            print("\n*** Please enter a number only ***")
            pass
        print("Please choose a unit from the list")
        for i in unit_options:
            print(f"{i} - {unit_options[i][0]}")
        print("Which unit?", end="\n")
        new_choice = input()
        if new_choice in (str(unit_options.keys())):
            new_choice = int(new_choice)
    return new_choice


def change_filter(sensor_list, active_sensors, sensors):
    """
    :param
        sensor_list:
            list of tuples (srt, srt, int)
        active_sensors:
            list of integers
        sensors:
            dictionary of sensor number names and int
    :return:
        void
    """
    switch = 1
    while(switch == 1):
        print_filter(recursive_sort(sensor_list), active_sensors)
        print("\nType the sensor number to toggle (e.g.4201) or x to end: ", end=' ')
        filter_input = input()
        if((filter_input == 'x') or (filter_input == 'X')):
            switch = 0
        if(filter_input in sensors.keys() or filter_input.lower() == "out"):
            if(filter_input.lower() == "out"):
                filter_input = "Out"
            if(sensors[filter_input] in active_sensors):
                active_sensors.remove(sensors[filter_input])
            elif(sensors[filter_input] not in sensors.keys()):
                active_sensors.append(sensors[filter_input])
        elif(filter_input == 'x' or filter_input == 'X'):
            pass
        elif(filter_input not in sensors.keys()):
            print("Invalid Sensor")


def print_summary_statistics(dataset, active_sensors):
    if not dataset:
        print("Please load data file and make sure at least one sensor is active")
    elif not active_sensors:
        print("Please load data file and make sure at least one sensor is active")
    print(dataset.get_summary_statistics(active_sensors))
    


def print_temp_by_day_time(dataset, active_sensors):
    print("Print Temp by Day/Time Function Called")


def print_histogram(dataset, active_sensors):
    print("Print Histogram Function Called")


def exit_program():
    print("Thank you for using the STEM Center Temperature Project")


class TempDataset:
    """ a class used to represent Temperature data

        Attributes
        _soc_sec : string
            the employee SSN
        _wage : float
            the employee's hourly wage
        _age : int
            the employee's age in years
    """
    __counter = int(0)
    

    def __init__(self):
        self._data_set = None
        self._name = "Unnamed"
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        """
        :param
            new_name:
                name for the dataset
        :return:
            void
        """
        if(len(new_name) < 3 or len(new_name) > 21 ):
            raise ValueError
        else:
            self._name = new_name

    def process_file(self, filename):
        self._data_set = []
        try:
            data_file = open(filename, 'r')
            self._data_set = []
            for next_line in data_file:
                pre_tup = next_line.strip("\n").strip(",").split(",")
                if(pre_tup[3] == "TEMP"):
                    pre_tup[0] = int(pre_tup[0])
                    pre_tup[1] = math.floor(float(pre_tup[1]) * 24)
                    pre_tup[2] = int(pre_tup[2])
                    pre_tup[4] = float(pre_tup[4])
                    pre_tup.remove("TEMP")
                    single_tuple = tuple(pre_tup)
                    self._data_set.append(single_tuple)
            data_file.close()
            return True
        except FileNotFoundError:
            print("File not found.")
            return False

    def get_summary_statistics(self, active_sensors):
        if(self._data_set == None):
            return None
        else:
            min = 1000
            max = 0
            avg_total = 0
            c = 0
            for i, (t1, t2, t3, t4) in enumerate(self._data_set):
                c += 1
                avg_total += t4
                if(t4 < min):
                    min = t4
                if(t4 > max):
                    max = t4
            avg_total = avg_total/c
            min = convert_units(min, current_unit)
            max = convert_units(max, current_unit)
            avg_total = convert_units(avg_total, current_unit)
            return (f"Summary statistics for {self.name} \n" + 
                f"Minimum Temperature: {round(min, 2)} {UNITS[current_unit][1]} \n" +
                f"Maximum Temperature: {round(max, 2)} {UNITS[current_unit][1]} \n" + 
                f"Average Temperature: {round(avg_total, 2)} {UNITS[current_unit][1]}")

    
    def get_avg_temperature_day_time(self, active_sensors, day, time):
        if(self._data_set == None or not active_sensors):
            return None
        elif(active_sensors):
            avg_value = 0
            c = 0
            for i, (t1, t2, t3, t4) in enumerate(self._data_set):
                if(t1 == day and t2 == time):
                    if(t3 in active_sensors):
                        avg_value += t4
                        c += 1
            return avg_value/c
        else:
            return 0

    def get_num_temps(self, active_sensors, lower_bound, upper_bound):
        if(self._data_set == None):
            return None
        else:
            return 0

    def get_loaded_temps(self):
        if(self._data_set == None or self._data_set == []):
            return None
        elif(self._data_set != []):
            return len(self._data_set)
        else: 
            return 0
            

    @classmethod
    def get_num_objects(cls):
        cls.__counter += 1
        return cls.__counter

def main():

    sensor_list = [
            ("4213", "STEM Center", 0),
            ("4201", "Foundations Lab", 1),
            ("4204", "CS Lab", 2),
            ("4218", "Workshop Room", 3),
            ("4205", "Tiled Room", 4),
            ("Out", "Outside", 5)
    ]
    sensors = {
            "4213": 0,
            "4201": 1,
            "4204": 2,
            "4218": 3,
            "4205": 4,
            "Out": 5
    }
    global UNITS 
    UNITS = {
        0: ("Celsius", "C"),
        1: ("Fahrenheit", "F"),
        2: ("Kelvin", "K")
    }
    current_set = TempDataset()
    global current_unit
    current_unit = 0
    active_sensors = [sensor_list[2] for sensor_list in sensor_list]
    print_header()
    exec_dict = {
        1 : new_file,
        2 : choose_units,
        3 : change_filter,
        4 : print_summary_statistics,
        5 : print_temp_by_day_time,
        6 : print_histogram,
        7 : exit_program
    }

    user_menu_input = 1
    while(user_menu_input != 7):
        print_menu()
        print(current_set.get_avg_temperature_day_time(active_sensors, 5, 7))
        print("What is your choice?", end = " ")
        user_menu_input = input()
        while(not isinstance(user_menu_input, int) or
              user_menu_input >= 8 or
              user_menu_input <= 0):
            try:
                user_menu_input = int(user_menu_input)
                if (user_menu_input >= 8 or user_menu_input <= 0):
                    print("\nInvalid Choice")
                    user_menu_input = input()
                    user_menu_input = int(user_menu_input)
            except:
                pass

            try:
                if (not isinstance(user_menu_input, int)):
                    print("\n*** Please enter a number only ***")
                    user_menu_input = input()
            except:
                pass

            try:
                user_menu_input = int(user_menu_input)
            except:
                pass

        if (user_menu_input == 1):
            exec_dict[user_menu_input](current_set)
        elif (user_menu_input == 2):
            current_unit = exec_dict[user_menu_input](current_unit, UNITS)
        elif (user_menu_input == 3):
            exec_dict[user_menu_input](sensor_list, active_sensors, sensors)
        elif (user_menu_input == 4):
            exec_dict[user_menu_input](current_set, current_set)
            current_set.get_avg_temperature_day_time(active_sensors, 5, 7)
        elif (user_menu_input == 5):
            exec_dict[user_menu_input](current_set, current_set)
        elif (user_menu_input == 6):
            exec_dict[user_menu_input](current_set, current_set)
        elif (user_menu_input == 7):
            exec_dict[user_menu_input]()


if __name__ == "__main__":
    main()

"""
STEM Center Temperature Project 
Nicholas Noochla-or

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

None
What is your choice? 4
Please load data file and make sure at least one sensor is active

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

None
What is your choice? 1
Please enter the filename of the new dataset: Temperatures2017-08-06.csv
Loaded 11724 samples
Please provide a 3 to 20 character name for the dataset Test Week

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

20.45544117647059
What is your choice? 4
Summary statistics for Test Week
Minimum Temperature: 16.55 C
Maximum Temperature: 28.42 C
Average Temperature: 21.47 C

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

20.45544117647059
What is your choice? 2
Current units in Celsius
Choose new units:
0 - Celsius
1 - Fahrenheit
2 - Kelvin
Which unit?
1

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

20.45544117647059
What is your choice? 4
Summary statistics for Test Week
Minimum Temperature: 61.79 F
Maximum Temperature: 83.16 F
Average Temperature: 70.64 F

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

20.45544117647059
What is your choice? 3

4201: Foundations Lab [ACTIVE]
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor number to toggle (e.g.4201) or x to end 4201

4201: Foundations Lab
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor number to toggle (e.g.4201) or x to end 4204

4201: Foundations Lab
4204: CS Lab
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor number to toggle (e.g.4201) or x to end x

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

19.910638297872342
What is your choice? 4
Summary statistics for Test Week
Minimum Temperature: 61.79 F
Maximum Temperature: 83.16 F
Average Temperature: 70.13 F

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

19.910638297872342
What is your choice? 3

4201: Foundations Lab
4204: CS Lab
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor number to toggle (e.g.4201) or x to end 4205

4201: Foundations Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor number to toggle (e.g.4201) or x to end 4213

4201: Foundations Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor number to toggle (e.g.4201) or x to end 4218

4201: Foundations Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center
4218: Workshop Room
Out: Outside [ACTIVE]

Type the sensor number to toggle (e.g.4201) or x to end Out

4201: Foundations Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center
4218: Workshop Room
Out: Outside

Type the sensor number to toggle (e.g.4201) or x to end x

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

None
What is your choice? 4
Please load data file and make sure at least one sensor is active

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

None
What is your choice? 7
Thank you for using the STEM Center Temperature Project
"""