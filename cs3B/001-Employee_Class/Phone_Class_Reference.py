class Contact:
    """ example that uses an inner (nested) class """
 
    # class ("static") members and intended constants
    DEFAULT_NAME = "(no name assigned)"
    MIN_NAME_LEN = 2
    MAX_NAME_LEN = 30
    DEFAULT_PH_NUM = "0001112222"
 
    # initializer ("constructor") method -------------------------------
    def __init__(self,
                 the_name=DEFAULT_NAME, the_ph_num=DEFAULT_PH_NUM):
        # instance (attributes
        if not self.set_name(the_name):
            self.name = Contact.DEFAULT_NAME
 
        # since this calls Phone constructor, we need not test return val
        self.phone = self.Phone(the_ph_num)
 
    # mutator ("set") methods ------------------------------------------
    def set_name(self, the_name):
        if type(the_name) != str \
                or \
                not (Contact.MIN_NAME_LEN <= len(the_name) <= Contact.MAX_NAME_LEN):
            return False
        # else
        self.name = the_name
        return True
 
    # sets the phone  from client **string**, not from Phone object
    def set_phone(self, the_ph_str):
        if not self.phone.set_phone_num(the_ph_str):
            return False
        # else
        return True  # if good param, mutator call already set
 
    # accessor ("get") methods ----------------------------------------
    def get_name(self):
        return self.name
 
    # returns the phone **string**, which most clients would expect
    def get_phone(self):
        return self.phone.to_string()
 
    # returns the phone **object**, if client wants that level of detail
    def get_phone_object(self):
        return self.phone
 
    # BEGIN INNER CLASS Phone -------------------------------------------
    class Phone:
        """ Phone is nested in Contact """
 
        # class ("static") members and intended constants
        DEFAULT_NUM = "7778889999"
        VALID_NUM_LEN = 10
 
        # initializer ("constructor") method --------------------------
        def __init__(self, the_num=DEFAULT_NUM):
 
            # instance attributes
            if not self.set_phone_num(the_num):
                self.ph_num = Contact.DEFAULT_PH_NUM
 
        # mutator method --------------------------
        def set_phone_num(self, the_ph_str):
 
            # first check that it's a string
            if type(the_ph_str) != str:
                return False
            # throw away non-numerics
            pure_number = self.extract_numeric_digits(the_ph_str)
            # check length
            if len(pure_number) != Contact.Phone.VALID_NUM_LEN:
                return False
 
            # else (passed all tests)
            self.ph_num = pure_number
            return True
 
        # accessor methods --------------------------
        def get_phone_num(self):
            return self.ph_num
 
        def to_string(self):
            """ turn '1234567890' into '(123)456-7890' """
 
            # build slowly for clarity -- could be done in one long statement
            ret_str = "("
            ret_str += self.ph_num[0:3]
            ret_str += ")"
            ret_str += self.ph_num[3:6]
            ret_str += "-"
            ret_str += self.ph_num[6:10]
 
            return ret_str
 
        # helper for vetting Phone numbers  --------------------------
        @staticmethod
        def extract_numeric_digits(the_num):
            """ store only digits '213-555-1212' becomes '2135551212'
                returns None if non-string, else
                the string minus non-numerics """
            if type(the_num) != str:
                return None
            # else
            the_length = len(the_num)
            number = ""
            for k in range(0, the_length):
                next_digit = the_num[k]
                if next_digit.isdigit():
                    number = number + next_digit
            return number
 
    # END INNER CLASS Phone -------------------------------------------
 
 
# client --------------------------------------------
 
# instantiate some Contacts with illegal and default phone nums #s ...
con_1 = Contact("Harsha", "234")
con_2 = Contact("Alfonso")
 
print("Nested class objects instantiated directly from main -----:")
bad_phone = Contact.Phone("bad bad number")
default_phone = Contact.Phone()
print(" Bad param gets Contact default: " + bad_phone.get_phone_num()
      + "\n No param gets Phone default: " + default_phone.get_phone_num())
 
# show the Contacts right after instantiation ---------------------
print("\nBefore mutators -------------------:")
print(("Contact #1:"
       + "\n    name: {}"
       + "\n    phone: {}").
      format(con_1.get_name(),
             con_1.get_phone()))
print(("Contact #2:"
       + "\n    name: {}"
       + "\n    phone: {}").
      format(con_2.get_name(),
             con_2.get_phone()))
 
# try to mutate some Contact objects, legally and illegally
con_1.set_name("Stephen Hawking")  # should work
 
# ok to access either the Contact mutator or the Contact.Phone mutator
con_1.set_phone("(605)  555-1212")  # should work
con_1.phone.set_phone_num("123-3333")  # should fail - too short
 
# contact #2 setters invoked (one good, one bad):
con_2.set_name("waytoolong waytoolong waytoolong")  # should fail
con_2.phone.set_phone_num("123-456-7890")  # should work
 
# show the Contacts  after mutator calls  ---------------------
print("\nAfter mutators -------------------:")
print(("Contact #1:"
       + "\n    name: {}"
       + "\n    phone: {}").
      format(con_1.get_name(),
             con_1.get_phone()))
print(("Contact #2:"
       + "\n    name: {}"
       + "\n    phone: {}").
      format(con_2.get_name(),
             con_2.get_phone()))
 
# compare the two get_phone_xxx() accessors  ---------------------
show_me = con_1.get_phone()
print("\nResult of get_phone(): ", show_me)
show_me = con_1.get_phone_object()
print("\nResult of get_phone_object(): ", show_me,
      "\n(that was ugly...)")
print("(Better things to do with the returned object): \n",
      show_me.get_phone_num(),
      "\n      or \n",
      show_me.to_string())