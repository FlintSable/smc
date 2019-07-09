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
        print(client_intro_str + str(self))

    # standard python stringizer ------------------------
    def __str__(self):
        return self.to_string()

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


# client --------------------------------------------

# instantiate some students, one with and illegal name ...  
my_students = \
    [
        Student("smith", "fred", 95),
        Student("bauer", "jack", 123),
        Student("jacobs", "carrie", 195), Student("renquist", "abe", 148),
        Student("3ackson", "trevor", 108), Student("perry", "fred", 225),
        Student("loceff", "fred", 44), Student("stollings", "pamela", 452),
        Student("charters", "rodney", 295), Student("cassar", "john", 321)
    ]

array_size = len(my_students)
StudentArrayUtilities.print_array(my_students, "\nBefore last-name sort:")
StudentArrayUtilities.array_sort(my_students, array_size)
StudentArrayUtilities.print_array(my_students, "\nAfter last-name sort: ")

"""  ---------------------- RUN ------------------------

Before last-name sort:
 ---------- 
    name: smith, fred
    total points: 95.
 ---------- 
    name: bauer, jack
    total points: 123.
 ---------- 
    name: jacobs, carrie
    total points: 195.
 ---------- 
    name: renquist, abe
    total points: 148.
 ---------- 
    name: zz-error, trevor
    total points: 108.
 ---------- 
    name: perry, fred
    total points: 225.
 ---------- 
    name: loceff, fred
    total points: 44.
 ---------- 
    name: stollings, pamela
    total points: 452.
 ---------- 
    name: charters, rodney
    total points: 295.
 ---------- 
    name: cassar, john
    total points: 321.

After last-name sort: 
 ---------- 
    name: bauer, jack
    total points: 123.
 ---------- 
    name: cassar, john
    total points: 321.
 ---------- 
    name: charters, rodney
    total points: 295.
 ---------- 
    name: jacobs, carrie
    total points: 195.
 ---------- 
    name: loceff, fred
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
------------------------------------------------------------- """