#Write a program to convert a binary number to a decimal number without using the built-in function provided by Python.
# Note that you need to check the input is a binary number or not. 



n= int(input("Enter a binary number (with 0 and 1's) : "))
decimal, i = 0, 0
not_binary = False
while n > 0:
    rem = n%10
    if rem > 1 :
        not_binary = True
        break
    n//=10
    
    decimal += (rem*pow(2,i))
    i +=1
    
if not_binary:
    print("Invalid input !!!")
else:
    print("The decimal number is {} ".format(decimal))