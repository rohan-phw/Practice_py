#Print the following triangle of the following form with n rows for a given n i.e., 
# the first row contains n stars and next row with n-1 starts, and so on. 
# Note that you are allowed to use only one while loop (nested loops are not allowed).


x = eval(input("Enter no. of lines : "))
while(x>=1):
    print(x*"*",end=" ")
    print("\n")
    x -=1