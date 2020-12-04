#Write a program to print the following pattern for a given number of lines.


num_lines = int(input("Enter number of lines:\n"))

count=num_lines-1
while count>=0:
    print('  '*count,end= '')
    print('* '*(num_lines-count))
    
    count -=1
