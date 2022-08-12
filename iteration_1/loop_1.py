
'''
1. Write a program to print all Natural numbers from 1 to N where you have to take N as input from user

sol :
userNumber = int(input())
count = 1
while userNumber >= count:
    print(count,end=" ")
    count = count + 1
    
    
2. Write a program to print all odd numbers from 1 to N where you have to take N as input from user.

sol : 
userNumber = int(input())
initialNumber = 1
while userNumber >= initialNumber:
    if initialNumber % 2 != 0 :
        print(initialNumber,end= " ")
    initialNumber = initialNumber + 1
    
3. Write a program to find sum all Natural numbers from 1 to N where you have to take N as input from user

sol : 

userNumber = int(input())
total = 0
while userNumber >= 1 :
    total = total + userNumber
    userNumber = userNumber - 1
print(total)
    
    
    
4. Write a program to print all even numbers from 1 to N where you have to take N as input from user.

[Note : Use while-loop OR for-loop, according to session flow.]

sol : 
userNumber  = int(input())
initialNumber = 1
while userNumber >= initialNumber :
    if initialNumber % 2 == 0:
        print(initialNumber, end = " ")
    initialNumber = initialNumber + 1
    
5. Write a program to print all Natural numbers from N to 1 where you have to take N as input from user

sol : 
userNumber = int(input())
while userNumber >= 1:
    print(userNumber,end=" ")
    userNumber -= 1
    
    
    
6. You are given a positive integer A. You have to print the sum of all odd numbers in the range [1, A].

sol : 
userNumber = int(input())
total = 0
while userNumber >= 1:
    if userNumber % 2 != 0:
        total = total + userNumber
    userNumber -= 1
print(total)



7. Given an integer A, you have to tell whether it is a prime number or not.

A prime number is a natural number greater than 1 which is divisible only by 1 and itself.

sol : 

userNumber = int(input())

if userNumber <= 1:
    print("NO")
else:
    count = 2
    boundry = (userNumber//2)+1

    while count < boundry:
        if userNumber % count ==0:
            print("NO")
            break
        count+=1
    else:
        print("YES")
 

8. You are given two integers A and B. You have to find the value of AB.

NOTE: The value of answer is always less than or equal to 109.


sol : 
baseNumber  = int(input())
power = int(input())

print(baseNumber**power)


9. For a given number A, print its multiplication table having the first 10 multiples.

sol : 
userNumber = int(input())
initialNumber = 1

while initialNumber <= 10:
    print(userNumber ,"*", initialNumber , "=", initialNumber * userNumber)
    initialNumber = initialNumber + 1

10. Write a program to calculate the percentage (according to marks of a student) and grade (according to the percentage of a student). Five numbers(A, B, C, D & E) represent the marks of a student in 5 subjects which are out of 100. Print the percentage and the grade of the student.

If percentage >= 90% : Grade A
If percentage >= 80% but <90 : Grade B
If percentage >= 70% but <80: Grade C
If percentage >= 60% but <70: Grade D
If percentage >= 40% but <60: Grade E
If percentage < 40%: Grade F
NOTE: You have to take the lowest integer of the percentage. E.g. 90.8% will be treated as 90%.



sol : 

s1 = int(input())
s2 = int(input())
s3 = int(input())
s4 = int(input())
s5 = int(input())

percentage = (s1+s2+s3+s4+s5)/5

if percentage >= 90:
    print(int(percentage),"A", sep="\n")
elif percentage < 90 and percentage >= 80 :
    print(int(percentage),"B", sep="\n")
elif percentage < 80 and percentage >= 70 :
    print(int(percentage),"C", sep="\n")
elif percentage < 70 and percentage >= 60 :
    print(int(percentage),"D", sep="\n")
elif percentage < 60 and percentage >= 40 :
    print(int(percentage),"E", sep="\n")
else:
    print(int(percentage),"F", sep="\n")




11. You have been given a dataset for marks of 2 subjects, scored by students of classes ClassA and ClassB. 
You now want to compare the performances of class A and class B by finding out the average performance of the classes.
Write a program to find if class A performed better. 
Print True is Class A is strictly better else return False.


sol : 

s1 = int(input())
s2 = int(input())
s3 = int(input())
s4 = int(input())

averageOfClassA = (s1+s2)/2
averageOfClassB = (s3+s4)/2

if averageOfClassA > averageOfClassB :
    print("True")
else:
    print("False")
    
    
 12. Write a program to input three numbers(A, B & C) from user and print the maximum element among A, B & C in each line.
 
 sol : 
 
A = int(input())
B = int(input())
C = int(input())

if A >= B and A >= C :
    print(A)
elif A >= C and B >= C :
    print(B)
else:
    print(C)
    
    
 13.  Write a program to input three numbers(A, B & C) from user and print the minimum element among A, B & C in each line.
 
 sol :
A = int(input())
B = int(input())
C = int(input())

if A <= B and A <= C:
    print(A)
elif A <= C and B <= C:
    print(B)
else:
    print(C)
    
 14. You are given an integer A.

You have to tell how many days are there in the month denoted by A in a non-leap year.

Months are denoted as follows:

January : 1
February : 2
March : 3
April : 4
May : 5
June : 6
July : 7
August : 8
September : 9
October : 10
November : 11
December : 12


sol : 

month = int(input())

if month == 1:
    print("31")
elif month == 2:
    print("28")
elif month == 3:
    print("31")
elif month == 4:
    print("30")
elif month == 5:
    print("31")
elif month == 6:
    print("30")
elif month == 7:
    print("31")
elif month == 8:
    print("31")
elif month == 9:
    print("30")
elif month == 10:
    print("31")
elif month == 11:
    print("30")
elif month == 12:
    print("31")




'''



















