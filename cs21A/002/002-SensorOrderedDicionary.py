""" Assignment One: Opening Lines
    Author: Nicholas Noochla-or
    Date: 7/17/2019

    Enhancements in this release:
    - created and populated the sensors ordered dictionary
    - populated filter_list from sensors using list comprehention
    - implemented print_filter()
    - implemented change_filter()
    - implemented sensor_sort() with lambda expression
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
        "7 - Quit\n\n" +


        "What is your choice? ")
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


def new_file():
    print("Option 1 selected")


def choose_units():
    print("Option 2 selected")


def change_filter(sensors, filter_list, sensor_lookup):
    """
    :param
        sensor_list:
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
    

def show_summary():
    print("Option 4 selected")


def show_temp_date_time():
    print("Option 5 selected")


def show_histogram():
    print("Option 6 selected")


def exit_program():
    print("Thank you for using the STEM Center Temperature Project")


def main():

    print_header()
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

    filter_list = [x[1][1] for x in list(sensors.items())]
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
        user_menu_input = input()

        while(not isinstance(user_menu_input, int) or
              user_menu_input >= 8 or
              user_menu_input <= 0):
            try:
                user_menu_input = int(user_menu_input)
                if (user_menu_input >= 8 or user_menu_input <= 0):
                    print("Invalid Choice")
                    print_menu()
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
            exec_dict[user_menu_input]()
        elif (user_menu_input == 2):
            exec_dict[user_menu_input]()
        elif (user_menu_input == 3):
            exec_dict[user_menu_input](sensors, filter_list, sensor_lookup)
        elif (user_menu_input == 4):
            exec_dict[user_menu_input]()
        elif (user_menu_input == 5):
            exec_dict[user_menu_input]()
        elif (user_menu_input == 6):
            exec_dict[user_menu_input]()
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

Type the sensor number to toggle (e.g.4201) or x to end 4201 4201


4201: Foundations Lab
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor number to toggle (e.g.4201) or x to end 4201 4205


4201: Foundations Lab
4204: CS Lab [ACTIVE]
4205: Tiled Room
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor number to toggle (e.g.4201) or x to end 4201 4205


4201: Foundations Lab
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor number to toggle (e.g.4201) or x to end 4201 400
Invalid Sensor


4201: Foundations Lab
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor number to toggle (e.g.4201) or x to end 4201 x


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