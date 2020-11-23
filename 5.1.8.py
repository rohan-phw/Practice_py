#Write a Python Program to Check Triangle is Valid or Not using user specified angles. 
# Remember, any triangle is valid, if sum of three angles in a triangle is equal to 180. 
# Also, you need to check whether any of the angle is zero or not.

a_1 = int(input())
a_2 = int(input())
a_3 = int(input())

a_t = a_1 + a_2 + a_3

if (a_t == 180) and (a_1 !=0) and (a_2 != 0)and (a_3 != 0):
    print("It is a valid triangle !")
else :
    print("It is an invalid Triangle :(")

