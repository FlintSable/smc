# beginning of class Student definition -------------------------
class Student:
    # class ("static") members and intended constants
    DEFAULT_NAME = "zz-error"
    DEFAULT_POINTS = 0
    MAX_POINTS = 30

    # initializer ("constructor") method -------------------
    def __init__(self,
                 last=DEFAULT_NAME,
                 first=DEFAULT_NAME,
                 points=DEFAULT_POINTS):
        # instance attributes
        if not self.set_last_name(last):
            self.last_name = Student.DEFAULT_NAME
        if not self.set_first_name(first):
            self.first_name = Student.DEFAULT_NAME
        if not self.set_points(points):
            self.total_points = Student.DEFAULT_POINTS

    # mutator ("set") methods -------------------------------
    def set_last_name(self, last):
        if not self.valid_string(last):
            return False
        # else
        self.last_name = last
        return True

    def set_first_name(self, first):
        if not self.valid_string(first):
            return False
        # else
        self.first_name = first
        return True

    def set_points(self, points):
        if not self.valid_points(points):
            return False
        # else
        self.total_points = points
        return True

    # accessor ("get") methods -------------------------------
    def get_last_name(self):
        return self.last_name

    def get_first_name(self):
        return self.first_name

    def get_total_points(self):
        return self.total_points

    # output method  ----------------------------------------
    def display(self, client_intro_str="--- STUDENT DATA ---"):
        print(self.to_string(client_intro_str))

    # instance helpers -------------------------------
    def to_string(self, optional_title=" ---------- "):
        ret_str = ((optional_title
                    + "\n    name: {}, {}"
                    + "\n    total points: {}.").
                   format(self.last_name, self.first_name,
                          self.total_points))
        return ret_str

    # static/class methods -----------------------------------
    @staticmethod
    def valid_string(test_str):
        if (len(test_str) > 0) and test_str[0].isalpha():
            return True
        return False

    @classmethod
    def valid_points(cls, test_points):
        if 0 <= test_points <= cls.MAX_POINTS:
            return False
        else:
            return True

    @classmethod
    def compare_two_students(cls, first_stud, second_stud):
        """ comparison done on parameters' last names """
        return cls.compare_strings_ignore_case(
            first_stud.last_name, second_stud.last_name)

    @staticmethod
    def compare_strings_ignore_case(first_string, second_string):
        """ returns -1 if first < second, lexicographically,
           +1 if first > second, and 0 if same
           this particular version based on last name only
           (case insensitive) """

        fst_upper = first_string.upper()
        scnd_upper = second_string.upper()
        if fst_upper < scnd_upper:
            return -1
        # else if
        if fst_upper > scnd_upper:
            return 1
        # else
        return 0


# beginning of class StudentArrayUtilities definition ---------------
class StudentArrayUtilities:
    @staticmethod
    def print_array(stud_array,
                    optional_title="--- The Students -----------:\n"):

        print(optional_title)
        for student in stud_array:
            print(student.to_string())

    @classmethod
    def array_sort(cls, data, array_size):
        """ a simple bubble sort """
        for k in range(array_size):
            if not cls.float_largest_to_top(data, array_size - k):
                return

    @staticmethod
    def float_largest_to_top(data, array_size):

        changed = False

        # notice we stop at array_size - 2 because of expr. k + 1 in loop
        for k in range(array_size - 1):
            if Student.compare_two_students(data[k], data[k + 1]) > 0:
                data[k], data[k + 1] = data[k + 1], data[k]
                changed = True

        return changed

    NOT_FOUND = -1  # static constant best defined at top of class

    @classmethod
    def array_search(cls, data, array_size, key_first, key_last):
        for k in range(array_size):
            if (data[k].get_last_name() == key_last
                    and data[k].get_first_name() == key_first):
                return k  # found match, return index
        return cls.NOT_FOUND

    @classmethod
    def binary_search_for_last_name(cls, data, key_last_nm,
                                    first_index, last_index):
        # exhuasted search
        if first_index > last_index:
            return cls.NOT_FOUND

        middle_index = int((first_index + last_index) / 2)

        result = Student.compare_strings_ignore_case(
            key_last_nm,
            data[middle_index].get_last_name()
        )

        # < 0 means key before middle index
        if result < 0:
            return cls.binary_search_for_last_name(
                data, key_last_nm, first_index, middle_index - 1)

        # > 0 means key after middle index
        if result > 0:
            return cls.binary_search_for_last_name(
                data, key_last_nm, middle_index + 1, last_index)

        # else key IS in middle index position, i.e., found him
        return middle_index


# client --------------------------------------------

# instantiate some students, one with an illegal name ...  
my_students = \
    [
        Student("smith", "fred", 95),
        Student("bauer", "jack", 123),
        Student("jacobs", "carrie", 195),
        Student("renquist", "abe", 148),
        Student("3ackson", "trevor", 108),
        Student("perry", "fred", 225),
        Student("lewis", "frank", 44),
        Student("stollings", "pamela", 452)
    ]
array_size = len(my_students)
StudentArrayUtilities.array_sort(my_students, array_size)
StudentArrayUtilities.print_array(my_students, "Array to be searched: ")

print()

# search for two names in the list
last_name = "jacobs"
found = StudentArrayUtilities.binary_search_for_last_name(my_students,
                                                          last_name,
                                                          0, array_size - 1)
if found != StudentArrayUtilities.NOT_FOUND:
    print(last_name + " IS in list at position " + str(found))
else:
    print(last_name + " is NOT in list.")

last_name = "Stollings"
found = StudentArrayUtilities.binary_search_for_last_name(my_students,
                                                          last_name,
                                                          0, array_size - 1)
if found != StudentArrayUtilities.NOT_FOUND:
    print(last_name + " IS in list at position " + str(found))
else:
    print(last_name + " is NOT in list.")

# search for someone NOT in the list
last_name = "hendry"
found = StudentArrayUtilities.binary_search_for_last_name(my_students,
                                                          last_name,
                                                          0, array_size - 1)
if found != StudentArrayUtilities.NOT_FOUND:
    print(last_name + " IS in list at position " + str(found))
else:
    print(last_name + " is NOT in list.")

"""  ---------------------- RUN ------------------------

Array to be searched: 
 ---------- 
    name: bauer, jack
    total points: 123.
 ---------- 
    name: jacobs, carrie
    total points: 195.
 ---------- 
    name: lewis, frank
    total points: 44.
 ---------- 
    name: perry, fred
    total points: 225.
 ---------- 
    name: renquist, abe
    total points: 148.
 ---------- 
    name: smith, fred
    total points: 95.
 ---------- 
    name: stollings, pamela
    total points: 452.
 ---------- 
    name: zz-error, trevor
    total points: 108.

jacobs IS in list at position 1
Stollings IS in list at position 6
hendry is NOT in list.

------------------------------------------------------------- """