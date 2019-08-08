""" Assignment five: Print Summary Statistics
    Author: Nicholas Noochla-or
    Date: 8/7/2019

    Enhancements in this release:
    -
    -
    -

    Review (NN note):
    - review data not loaded condition
    - units, rankie
"""

import math

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

    """
    output = (
        "\n\nMain Menu\n" +
        "---------\n" +
        "1 - Process a new data file\n" +
        "2 - Choose units\n" +
        "3 - Edit room filter\n" +
        "4 - Show summary statistics \n" +
        "5 - Show temperature by date and time\n" +
        "6 - Show histogram of temperatures\n" +
        "7 - Quit\n\n")
    print(output, end="")
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


def sensor_sort(sensor_details, sort_by=0):
    """
    :param
        sensor_dict:
            dictionary of sensors
        sort_by(optional):
            used to select what value to sort by
    :return
        a sorted list of tuples by room number

    """
    slist = list(sensor_details.items())
    slist = [(k,v1[0], v1[1]) for k,v1 in sensor_details.items()]
    return sorted(slist, key = lambda the_tuple: the_tuple[sort_by])


def print_filter(sensor_list, filter_list):
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
        filter_list:
            list of integers
    :return:
        void
    """
    print("\n")
    for i, (t1, t2, t3) in enumerate(sensor_list):
        if(t3 in filter_list):
            print(f'{t1}: {t2} [ACTIVE]')
        else:
            print(f'{t1}: {t2}')


def new_file(dataset):
    try:
        print("Please enter the filename of the new database:", end=" ")
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
        print("File not found, coubld not open file")
        return False


def choose_units(current_unit, unit_options):
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


def change_filter(sensors, filter_list, sensor_lookup):
    """
    :param
        sensors:
            list of tuples (srt, srt, int)
        filter_list:
            list of integers
    :return:
        void
    """    
    switch = 1
    while(switch == 1):
        print_filter(sensor_sort(sensors), filter_list)
        print("\nType the sensor number to toggle (e.g.4201) or x to end 4201", end=' ')
        filter_input = input()
        if((filter_input == 'x') or (filter_input == 'X')):
            switch = 0
        if(filter_input in sensor_lookup.keys() or filter_input.lower() == "out"):
            if(filter_input.lower() == "out"):
                filter_input = "Out"
            if(sensor_lookup[filter_input] in filter_list):
                filter_list.remove(sensor_lookup[filter_input])
            elif(sensor_lookup[filter_input] not in sensor_lookup.keys()):
                filter_list.append(sensor_lookup[filter_input])
        elif(filter_input == 'x' or filter_input == 'X'):
            pass
        elif(filter_input not in sensor_lookup.keys()):
            print("Invalid Sensor")


def show_summary(dataset, sensor_list):
    if not dataset:
        print("Please load data file and make sure at least one sensor is active")
    elif not sensor_list:
        print("Please load data file and make sure at least one sensor is active")
    print(dataset.get_summary_statistics(sensor_list))


def show_temp_date_time(dataset, active_sensors):
    print("Print Temp by Day/Time Function Called")


def show_histogram(dataset, active_sensors):
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
        self._name = "Unnamed"
        self._data_set = None

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
            return (f"Summary statistics for {self._name} \n" + 
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

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if(len(new_name) < 3 or len(new_name) > 21):
            return False
        else:
            self._name = new_name
            return True

    @classmethod
    def get_num_objects(cls):
        cls.__counter += 1
        return cls.__counter

def main():
    sensors = {
            "4213": ("STEM Center" , 0),
            "4201": ("Foundations Lab", 1),
            "4204": ("CS Lab", 2),
            "4218": ("Workshop Room", 3),
            "4205": ("Tiled Room", 4),
            "Out": ("Outside", 5)
    }

    sensor_lookup = {
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
    current_set  = TempDataset()
    global current_unit
    current_unit = 0
    filter_list = [x[1][1] for x in list(sensors.items())]
    print_header()
    exec_dict = {
        1 : new_file,
        2 : choose_units,
        3 : change_filter,
        4 : show_summary,
        5 : show_temp_date_time,
        6 : show_histogram,
        7 : exit_program
    }

    user_menu_input = 1
    while(user_menu_input != 7):
        print_menu()
        print(current_set.get_avg_temperature_day_time(filter_list, 5, 7))
        print("What is your choice?", end = " ")
        user_menu_input = input()
        while(not isinstance(user_menu_input, int) or
              user_menu_input >= 8 or
              user_menu_input <= 0):
            try:
                user_menu_input = int(user_menu_input)
                if (user_menu_input >= 8 or user_menu_input <= 0):
                    print("Invalid Choice")
                    # print_menu()
                    user_menu_input = input()
                    user_menu_input = int(user_menu_input)
            except:
                continue

            try:
                if (not isinstance(user_menu_input, int)):
                    print("*** Please enter a number only ***")
                    print_menu()
                    user_menu_input = input()
            except:
                continue

            try:
                user_menu_input = int(user_menu_input)
            except:
                continue

        if (user_menu_input == 1):
            exec_dict[user_menu_input](current_set)
        elif (user_menu_input == 2):
            current_unit = exec_dict[user_menu_input](current_unit, UNITS)
        elif (user_menu_input == 3):
            exec_dict[user_menu_input](sensors, filter_list, sensor_lookup)
        elif (user_menu_input == 4):
            exec_dict[user_menu_input](current_set, current_set)
            current_set.get_avg_temperature_day_time(filter_list, 5, 7)
        elif (user_menu_input == 5):
            exec_dict[user_menu_input](current_set, current_set)
        elif (user_menu_input == 6):
            exec_dict[user_menu_input](current_set, current_set)
        elif (user_menu_input == 7):
            exec_dict[user_menu_input]()

if __name__=="__main__":
    main()

"""




"""