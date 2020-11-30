# Suppose that you are assigned a task to find the maximum element in a given set of positive integers.  
# But, you are not given the whole input at a time, and the data comes in the streaming process. 
# Further, the data ends with a non-positive element. 
# You are supposed to compute the maximum element that you are given until the current position. 
# Also, you are given only two variables to store the information, one is to store the current input value, 
# and other is to save the maximum till current input.  
# Write a python program to perform the above task.  

print("Enter the number of students:")
n=int(input())
sum=0
mm=[]
for i in range(n):
    m=int(input())
    mm.append(m)
    sum+=m
print("marks of students in ECSE 105L:",mm)
print("avg. marks secured in the subject:","{:.2f}".format(sum/n))