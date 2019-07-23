""" Assignment Dataset Class
    Author: Nicholas Noochla-or
    Date: 7/22/2019

    Enhancements in this release:
    - created and populated the sensors ordered dictionary
    Create an object of type TempDataset(). 
    Load temperature data into that object
    Name our dataset and ask for its name
    Ask for the number of temperature samples in the dataset
    Ask for the number of temperature samples within a certain range
    Ask for the average temperature for a particular day of the week and hour of the day
    Get the minimum, average and maximum temperature as a tuple
    Find out how many objects of TempDataset() have been created

"""


def main():

    current_set = TempDataset()
    current_set1 = TempDataset()
    current_set2 = TempDataset()
    print(current_set2.get_num_objects())

    current_set3 = TempDataset()
    print(current_set3.get_num_objects())

    # current_set.set_name("New Name")
    # print(current_set.get_name())

    # if not current_set.set_name("New Name"):
    #     print("Fail")
    # elif current_set.get_name() == "New Name":
    #     print("Success")
    # else:
    #     print("Fail")

    # print("First test of get_num_objects: ", end='')

    # if TempDataset.get_num_objects() == 1:
    #     print("Success")
    # else:
    #     print("Fail")

    # second_set = TempDataset()

    # print("Second test of get_num_objects: ", end='')

    # if TempDataset.get_num_objects() == 2:
    #     print("Success")
    # else:
    #     print("Fail")

    # print("Testing get_name and set_name: ")
    # print("- Default Name:", end='')

    # if current_set.get_name() == "Unnamed":
    #     print("Success")
    # else:
    #     print("Fail")

    # print("- Try setting a name too short: ", end='')

    # if current_set.set_name("to"):
    #     print("Fail")
    # elif not current_set.get_name() == "Unnamed":
    #     print("Fail")
    # else:
    #     print("Success")

    # print("- Try setting a name too long: ", end='')

    # if current_set.set_name("supercalifragilisticexpialidocious"):
    #     print("Fail")
    # elif not current_set.get_name() == "Unnamed":
    #     print("Fail")
    # else:
    #     print("Success")

    # print("- Try setting a name just right: ", end='')

    # if not current_set.set_name("New Name"):
    #     print("Fail")
    # elif current_set.get_name() == "New Name":
    #     print("Success")
    # else:
    #     print("Fail")

    # print("- Make sure we didn't touch the other object: ", end='')
    # if second_set.get_name() == "Unnamed":
    #     print("Success")
    # else:
    #     print("Fail")

    # print("Testing get_avg_temperature_day_time: ", end='')
    # if current_set.get_avg_temperature_day_time(None, 0, 0) is None:
    #     print("Success")
    # else:
    #     print("Fail")

    # print("Testing get_num_temps: ", end='')
    # if current_set.get_num_temps(None, 0, 0) is None:
    #     print("Success")
    # else:
    #     print("Fail")

    # print("Testing get_loaded_temps: ", end='')
    # if current_set.get_loaded_temps() is None:
    #     print("Success")
    # else:
    #     print("Fail")

    # print("Testing get_summary_statistics: ", end='')
    # if current_set.get_summary_statistics(None) is None:
    #     print("Success")
    # else:
    #     print("Fail")

    # print("Testing process_file: ", end='')
    # if current_set.process_file(None) is False:
    #     print("Success")
    # else:
    #     print("Fail")

class TempDataset:

    __counter = int(0)
    
    def __init__(self):
        self._name = "Unnamed"
        self._data_set = None
        TempDataset.__counter += 1
        
    
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

    # @property
    def get_name(self):
        return self._name
    
    # @get_name.setter
    def set_name(self, new_name):
        if(len(new_name) < 3 or len(new_name) > 21):
            return False
        else:
            self._name = new_name

    @classmethod
    def get_num_objects(cls):
        # cls.__counter += 1
        return cls.__counter
    

if __name__ == "__main__":
    main()

"""

"""