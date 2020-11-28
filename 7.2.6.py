#Write a Python program to construct the following pattern, using a nested for loop.
#Read the maximum number of *'s  from the user.
print("Enter the maximum no of *'s:")
print()
mx = int(input())
n = 1
while(n<=mx):
    for i in range(n):
        print('*', end=' ')
    print()
    n=n+1
n=n-2
while(n>=1):
    for i in range(n):
        print('*', end=' ')
    print()
    n=n-1