#Write a program to print all the multiples of 7 from 1 to n for a given positive integer.

n = eval(input())
i = 1
print("The multiples of 7 are : ")
while i <= n :
    if i%7==0:
        print(i)
    i=i+1
