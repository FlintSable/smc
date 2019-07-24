""" 

"""


def main():
    a_var = "global value"

    def outer():
        global a_var
        a_var = 'inner value'

    print(a_var)






if __name__ == "__main__":
    main()

"""

"""