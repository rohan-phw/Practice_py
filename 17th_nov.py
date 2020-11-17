#Write a program in Python that inputs data (class, age, marks in mathematics, science) about two persons- Ram and Shyam. The program uses relational operators to check whether they study in same class? Is Ram younger to Shyam? Is Ram’s marks in mathematics more than Shyam? Is Ram’s marks in science less than Ram? The answer by the program is either True or False. The operators to be used are: <, >, ==. 
#Sample input:
#R_class=XII
#S_class=XII
#R_age=18
#S_age=19
#R_math=80
#S_math=90
#R_sci=85
#S_sci=92

#Sample Output:
#Both are in same class ? True 
#Both are of different age ? True 
#Ram score more than Shyam in Math ? False 
#Ram score less than Shyam in Science ? True
#Ram score more or equal than Shyam in Math? False

R_class = int(input())
S_class = int(input())
R_age = int(input())
S_age = int(input())
R_math = int(input())
S_math = int(input())
R_sci = int(input())
S_sci = int(input())
if R_class == S_class :
    print("Both are in same class ? True")
if R_age != S_age :
    print("Both are of different age ? False")
if R_math < S_math :
    print("Ram scored less than Shyam in maths ?True")
if R_sci < S_sci :
    print("Ram scored equal to or more than Shyam in science ?False")