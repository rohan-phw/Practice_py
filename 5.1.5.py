#A shopkeeper in a village area near NCR purchases old products from a vender. 
# Later, at the time of sell, he realizes that some of the products don’t have market in his village. 
# So he needs to give offers and reduce the cost of these products. 
# So write a python program which allows the user to enter the Sales amount and Actual cost of a Product, 
# and calculates the Loss Amount or profit Amount based on those two values using if-else Statement.
cp = float(input())
sp = float(input())
if cp>sp:
    print("Total Loss=",cp-sp)
elif sp>cp:
    print("Total Profit=",sp-cp)
else:
    print("No profit no Loss")


