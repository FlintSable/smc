#!/usr/bin/env python3
<<<<<<< HEAD

import re

# looking for any reference to http
regex = r'((http?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)'

data = open("data.txt", "r")
read_data = data.read()
websites = re.findall(regex, read_data)
data.close()


print(websites)
=======
import re


def main():
    print("main")

>>>>>>> c6968ca839456ce9b117eb598622499fea8bf6b1
