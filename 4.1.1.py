#Write a Python program to read two integer X and Y from users and print three lines as output, where
#Line 1. Contains sum of both, i.e. X+Y
#Line 2. Contains exponential value, i.e. X**Y
#Line 3. Contains (X-Y)^2, i.e. X**2+Y**2-2*X*Y  (^ represents power in question).
x = eval(input())
y = eval(input())
print(x+y)
print(x**y)
print((x**2)+(y**2)-(2*x*y))

 