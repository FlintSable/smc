#!/usr/bin/env python3
# import matplotlib.pyplot as plt
import pandas as pd
import re

import pprint
pp = pprint.PrettyPrinter(indent=4)

def fileToDict(filedata):
    try:
        filedata = pd.read_csv(f"{filedata}", delimiter = "\t")

        # clean data
        filedata.drop_duplicates()

        outdata = filedata.groupby('email').apply(lambda x: x).to_dict()
        return outdata
    except:
        return []

def main():
    valid_file = False
    while not valid_file:
        user_filename = input("Please enter data filename: ")
        try:
            data = fileToDict(user_filename)
            # print(data)
            if len(data) > 0:
                valid_file = True
                print("data loaded")
            else:
                print("Please enter valid file")
            if valid_file == True:
                break
        except:
            print("could not load data")
            pass
    pp.pprint(data)

if __name__=="__main__":
    main()