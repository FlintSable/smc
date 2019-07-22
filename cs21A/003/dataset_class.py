""" Assignment Eight: Dataset Class - Nicholas Noochla-or
"""

def main():

    current_set = TempDataset()

    print("First test of get_num_objects: ", end='')

    if TempDataset.get_num_objects() == 1:
        print("Success")
    else:    
        print("Fail")
    
    second_set = TempDataset()

    print("Second test of get_num_objects: ", end='')

    if TempDataset.get_num_objects() == 2:    
        print("Success")
    else:    
        print("Fail")
    
    print("Testing get_name and set_name: ")

    print("- Default Name:", end='')

    if current_set.name == "Unnamed":    
        print("Success")
    else:    
        print("Fail")
    
    print("- Try setting a name too short: ", end='')

    try:
        current_set.name = "to"   
        print("Fail")
    except ValueError:
        print("Success")
    
    print("- Try setting a name too long: ", end='')

    try:
        current_set.name = "supercalifragilisticexpialidocious"
        print("Fail")
    except ValueError:
        print("Success")
    
    try:
        current_set.name = "New Name"
        if current_set.name == "New Name":
            print("Success")
        else:
            print("Fail")
    except ValueError:
        print("Fail")

    print("- Make sure we didn't touch the other object: ", end='')
    if second_set.name == "Unnamed":    
        print("Success")
    else:    
        print("Fail")
    
    print("Testing get_avg_temperature_day_time: ", end='')
    if current_set.get_avg_temperature_day_time(None, 0, 0) is None:    
        print("Success")
    else:    
        print("Fail")
    
    print("Testing get_num_temps: ", end='')
    if current_set.get_num_temps(None, 0, 0) is None:
        print("Success")
    else:
        print("Fail")

    print("Testing get_loaded_temps: ", end='')
    if current_set.get_loaded_temps() is None:
        print("Success")
    else:
        print("Fail")

    print("Testing get_summary_statistics: ", end='')
    if current_set.get_summary_statistics(None) is None:
        print("Success")
    else: 
        print("Fail")
    
    print("Testing process_file: ", end='')
    if current_set.process_file(None) is False:
        print("Success")
    else:
        print("Fail")


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
        return False
    
    def get_summary_statistics(self, active_sensors):
        if(self._data_set == None):
            return None
        else:
            return (0, 0, 0)
    
    def get_avg_temperature_day_time(self, active_sensors, day, time):
        if(self._data_set == None):
            return None
        else:
            return 0

    def get_num_temps(self, active_sensors, lower_bound, upper_bound):
        if(self._data_set == None):
            return None
        else:
            return 0

    def get_loaded_temps(self):
        if(self._data_set == None):
            return None
        else:
            return 0

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

    @classmethod
    def get_num_objects(cls):
        cls.__counter += 1
        return cls.__counter


if __name__ == "__main__":
    main()

"""
First test of get_num_objects: Success
Second test of get_num_objects: Success
Testing get_name and set_name: 
- Default Name:Success
- Try setting a name too short: Success
- Try setting a name too long: Success
Success
- Make sure we didn't touch the other object: Success
Testing get_avg_temperature_day_time: Success
Testing get_num_temps: Success
Testing get_loaded_temps: Success
Testing get_summary_statistics: Success
Testing process_file: Success
"""