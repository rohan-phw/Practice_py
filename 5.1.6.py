#Andhra Pradesh Power Corporation Limited supplies electricity to peoples of Andhra Pradesh. 
# They have four ranges of charges for all the residential connections. 
# The charges per unit with surcharge for different ranges of consumptions are given as follows.

#Unit Range	Rate per Unit	Surcharge
#0-50	       2.60	        25
#50-100	       3.25	        35
#100-200	   5.26	        45
#>200	       8.45	        75
#Write a python program using if else to calculate the bill for a user based on no. of unit consumed.

unit = float(input())
if (unit <= 50):
    print("Electricity Bill=",(unit*2.60)+35)
elif (unit > 50 and unit <100):
    print("Electricity Bill=",(50*2.60)+((unit-50)*3.25)+35)
elif (unit>100 and unit<200):
    print("Electricity Bill=",(50*2.60)+(50*3.25)+((unit-100)*5.26)+45)
else :
    print("Electricity Bill=",(50*2.60)+(50*3.25)+(100*5.26)+((unit-200)*8.45)+75)