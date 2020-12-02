#Write a program in Python to calculate and print the power m of a given number n without using ** operator or pow (n, m) function

n=int(input("Enter a number n:\n"))
m=int(input("Enter power m:\n"))
power=1
for i in range(1,m+1):
    power=power*n
print("power({},{}) = {}".format(n,m,power))
