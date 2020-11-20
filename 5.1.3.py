#As we know that dog’s life is much lower than human life. 
# Suppose your friend wants to estimate Dog’s life equivalence to dog's years. 
# So write a Python program to estimate a dog's age in dog's years. 

#Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
x = eval(input())
a = x - (x-2)
a_yrs = float(a*10.5)
b = x- a
b_yrs = b*4
total = a_yrs+b_yrs
if x<0 :
    print("This cannot be true!")
elif x==0 :
    print("This corresponds to 0 human years!")
else :
    print(int(total))    

 