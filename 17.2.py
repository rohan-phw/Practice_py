#Chulbul pandey is numerologer i.e. belief in relationship between numbers. 
# He decides to purchase the car and will decide the registration number by 
# calculating the sum of the digits (four digit rto number), 
# If the sum is greater than 12 than only he says yes. 
# Write a python program to implement the logic.
no = int(input())
a = no%10
b = (no//10)%10
c = (no//100)%10
d = (no//1000)%10

print("Chulbul agree for the number?", a+b+c+d > 12)

 