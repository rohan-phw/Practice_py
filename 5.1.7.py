#A class of 10+2 has large no. of students and taught student five subjects English, Math, Computer, Physics, and Chemistry. 
# Due to large no. of students, evaluation board has a hectic task to calculate percentage of marks obtained by students. 
# Therefore, write a python program to calculate Student Percentage. 
# For this, first, you have to calculate Total, and Percentage of Five Subjects. Next, use Elif to find the grade.

#The grade can be calculated as follows.

#>90	A
#81-90	B
#71-80	C
#61-70	D
#40-60	E
#Else	Fail

eng = eval(input())
math = eval(input())
comp = eval(input())
phy = eval(input())
chem = eval(input())
total_m = (eng+math+comp+phy+chem)
print("Total Marks= ",total_m)
perc = (total_m/500)*100
print("Marks Percentage= ",perc)

if (perc > 90):
    print("Grade= A")
elif (perc > 81 and perc < 90):
    print("Grade= B")
elif (perc > 71 and perc < 80):
    print("Grade= C")
elif (perc > 61 and perc < 70):
    print("Grade= D")
elif (perc > 40 and perc < 60):
    print("Grade= E")
else :
    print("FAIL")

