#Write a program to convert an Octal number to a decimal number without using the built-in function provided by Python. 
# Note that you need to check the input is a Octal number or not. 

a = int(input("Enter an Octal Number: "))
isInvalid = False

temp = a
while temp > 0:
    digit = temp % 10
    if digit >7:
        isInvalid = True
        break
    temp = int(temp//10)

if isInvalid:
    print("Invalid input !!!")
else:
    decimal_num, i = 0, 0
    while a >0:
        decimal_num += (a%10)*(8**i)
        a = int(a//10)
        i +=1
    print("The decimal number is", decimal_num)
