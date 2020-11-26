#Write a program to print Fibonacci series up to n numbers where n will be taken as input. 

#The Fibonacci series is 0,1,1,2,3,5,8,13… where first term is 0, 
# second term is 1 and the n-th term is the sum of (n-1)-th term and (n-2)-th term for all n >= 3.

n = int(input("Enter the n value: "))
a=0
b=1
total=0
count=1
print("Fibonacci series id :")
while(count<=n):
    print(total,end=" ")
    count=+1
    a=b
    b=total
    total=a+b
