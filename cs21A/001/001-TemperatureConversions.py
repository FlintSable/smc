""" Assignment One: Temperature Conversions - Nicholas Noochla-or
"""


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
        "7 - Quit\n\n" +

        "What is your choice? ")
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
    print("New File Function Called")


def choose_units():
    print("Choose Units Function Called")


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
    print("Summary Statistics Function Called")


def print_temp_by_day_time(dataset, active_sensors):
    print("Print Temp by Day/Time Function Called")


def print_histogram(dataset, active_sensors):
    print("Print Histogram Function Called")


def exit_program():
    print("Thank you for using the STEM Center Temperature Project")


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
            exec_dict[user_menu_input](None)
        elif (user_menu_input == 2):
            exec_dict[user_menu_input]()
        elif (user_menu_input == 3):
            exec_dict[user_menu_input](sensor_list, active_sensors, sensors)
        elif (user_menu_input == 4):
            exec_dict[user_menu_input](None, None)
        elif (user_menu_input == 5):
            exec_dict[user_menu_input](None, None)
        elif (user_menu_input == 6):
            exec_dict[user_menu_input](None, None)
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

What is your choice? 3


4201: Foundations Lab [ACTIVE]
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor number to toggle (e.g.4201) or x to end:  4201


4201: Foundations Lab
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor number to toggle (e.g.4201) or x to end:  4205


4201: Foundations Lab
4204: CS Lab [ACTIVE]
4205: Tiled Room
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor number to toggle (e.g.4201) or x to end:  400
Invalid Sensor


4201: Foundations Lab
4204: CS Lab [ACTIVE]
4205: Tiled Room
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor number to toggle (e.g.4201) or x to end:  x


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