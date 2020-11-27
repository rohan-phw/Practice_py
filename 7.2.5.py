#Given two integers N1 and N2, display the given number 
#pattern(Square number patterns).
n_1 = int(input())
n_2 = int(input())

while n_1 > 0 :
    num = 1
    while num <=2:
        if num != n_2:
            print(num, end=" ")
        else:
            print(num)
        num +=1
    n_1 -= 1      
