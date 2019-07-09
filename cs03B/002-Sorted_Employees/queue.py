# beginning of class MyStack definition -------------------------
import copy  # needed by MyStack - details in coming weeks


class Queue:
    # class ("static") members and intended constants
    MAX_SIZE = 100000
    DEFAULT_SIZE = 10
    EMPTY_STACK_RETURN_ALERT = "** attempt to remove from empty queue **"
    ORIG_DEFAULT_ITEM = ""
    default_item = ORIG_DEFAULT_ITEM

    # initializer ("constructor") method -------------------
    def __init__(self, capacity=DEFAULT_SIZE, default_item=None):

        self.tos = 0
        self.que = []
        # instance attributes
        if not self.set_capacity(capacity):
            self.capacity = Queue.DEFAULT_SIZE

        if default_item is not None:
            self.default_item = default_item

        # initialize an array of size=capacity for our stack, all to default_item
        # force stack to be empty by setting self.tos to 0
        # (all done in clear())
        self.clear()

    # mutators -------------------------------
    def set_capacity(self, capacity):
        if not Queue.valid_capacity(capacity):
            return False

        # else
        self.capacity = capacity
        self.clear()
        return True

    def add(self, item_to_add):
        if self.tos == self.capacity:
            return False
        elif type(item_to_add) != type(self.default_item):

            return False
        self.que[self.tos] = item_to_add
        self.tos -= 1
        return True

    def remove(self):
        if self.tos == 0:
            return self.EMPTY_STACK_RETURN_ALERT
        # else
        self.tos += 1
        return self.que[self.tos]

    def clear(self):
        """  remove all items from stack """
        # deepcopy() for mutable defaults - details later
        self.que = [copy.deepcopy(self.default_item)
                    for k in range(self.capacity)]
        self.tos = 0

    # accessors -------------------------------
    def get_capacity(self):
        return self.capacity

    # static/class methods ------------------------
    @classmethod
    def valid_capacity(cls, test_capacity):
        if not (0 <= test_capacity <= cls.MAX_SIZE):
            return False
        else:
            return True

    @classmethod
    def set_default_item(cls, new_default):
        """ this will change the default of newly instantiated stacks """
        cls.default_item = new_default


# client --------------------------------------------

# # instantiate two empty stacks, one of 50 ints, another of 15 strings 
# s1 = MyStack(50, -1)
# s2 = MyStack(15, "undefined")
# # and one more with bad argument
# s3 = MyStack(-100)

# # confirm the stack capacities
# print("------ Stack Sizes -------\n  s1: {}   s2: {}   s3: {}\n".
#       format(s1.get_capacity(), s2.get_capacity(), s3.get_capacity()))

# # test the stack -----
# print(s1.pop())
# print()

# s1.push(44)
# s1.push(123)
# s1.push(99)
# s2.push("bank")
# s2.push("-34")
# s1.push(10)
# s1.push(1000)

# # try to put a square peg into a round hole
# if not s1.push("should not be allowed into an int stack"):
#     print("Successfully rejected due to type incompatibility")
# if not s2.push(444):
#     print("Successfully rejected due to type incompatibility")
# if not s1.push(44.4):
#     print("Successfully rejected due to type incompatibility")

# # and here test return type if good argument
# if s2.push("should be okay"):
#     print("Successfully accepted a good type")

# s2.push("a penny earned")
# s2.push("item #9277")
# s2.push("where am i?")
# s2.push("4")

# print("\n--------- First Stack ---------\n")
# for k in range(0, 10):
#     print("[" + str(s1.pop()) + "]")

# print("\n--------- Second Stack ---------\n")
# for k in range(0, 10):
#     print("[" + str(s2.pop()) + "]")