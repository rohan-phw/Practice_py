#Write a Python program using if else statements to compare two given numbers using 
#six relational operators ==, !=, >, <, >=, and <=. 
#The program prints six lines of output by either if statement or else statement.

a = int(input())
b = int(input())
if (a != b) :
    print("A is not equal to B")
elif (a == b) :
    print("A is equal to B")
elif (a > b) :
    print("A is greater than B")
elif (b > a) :
    print("A is less thab B")
elif (a >= b) :
    print("A is either greater than B or equal to it")
else :
    print("A is either less than B or equal to it")

