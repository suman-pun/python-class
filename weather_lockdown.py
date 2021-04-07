#1. Make a program which takes user input and display either user input is leap year or not.
# # User input must be 4 digit integer
# # example: 2020 is leap year, 2021 is not
# Note: Program should ask for user input till user input is incorrect

num=int(input("Enter the leap year: "))
string_num=str(num)
while len(string_num)<5:
    if num%4==0:
         print("It is leap year")
         break
    else:
        reenter=int(input("It is not a leap year, enter again: "))
        if reenter%4==0:
            print("It is leap year")
            break
        else:
            continue


