""" 

"""


def main():

    various_nums = [77.5, 92, 80, -78.111, 690, 101.3, -3,1515927, 0.0003]

    for index in range( len(various_nums) ):
        row_out = "item #{} is {:15.3f}".format(index, various_nums[index])
        print(row_out)      
    # homes_for_sale = [ 
    #     ("123 main", 1.75, 5, 2500),
    #     ("37812 elm", 1.2, 17, 2190),
    #     ("55 n. 3rd", 0.975, 8, 1250),
    #     ("12345 el monte road", 4.5, 11, 9754)
    #     ]

    # print(sorted(homes_for_sale,key=lambda tup:tup[3]))


    # user_age = int(input( "How old are you? "))
    # if user_age < 0:
    #     print("Your age cannot be negative")
    #     print( "You say you're", user_age, "years old." )
    # while True:
    #     try:
    #         userChoice = int(input("Enter a number "))
    #     except:
    #         print("Hey, that's not a number!")
    #         continue
    #     twiceNumber = userChoice * 2
    #     print("Twice your number is", twiceNumber)





if __name__ == "__main__":
    main()

"""

"""