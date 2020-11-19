#Chulbul Pandey is titular cop in Gaziyabad, Utter Pradesh. 
# He arrested some of the theives during bank rabbery. 
# He has jolly nature personality and alwayes throughs different  conditions on criminals. 
# And sometimes offers freedom to them. So this time, he randmoly distribute jersies with jursy number. 
# Then, he put a condition on them that prisoners with Armstrong number on his jersey can go to his home but 
# reaming prisoners need to spend few more days to the prison. Therefore, write a Python program to identify 
# the Armstrong number. A number (abcd) is known as Armstrong number if sum of its digits cube equals to number, 
# i.e abcd..=a^3+b^3+c^3+d^3…
x = int(input())
a = x%10
b = (x//10)%10
c = (x//100)%10
if (a**3)+(b**3)+(c**3)==x :
    print("TRUE")
else :
    print("FALSE")

