#!/usr/bin/env python3


import re

# looking for any reference to http
regex = r'((http?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)'

data = open("data.txt", "r")
read_data = data.read()
websites = re.findall(regex, read_data)
data.close()


print(websites)
