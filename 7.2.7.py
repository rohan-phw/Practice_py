#Program to print hollow square star patterns:

num_lines = int(input())
for i in range(1, num_lines+1):
    if (num_lines % i) :
        print('*'+(' '*(num_lines-2)+'*'))
    else :
        print('*'*num_lines)


