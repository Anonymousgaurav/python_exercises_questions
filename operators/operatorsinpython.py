
"""
1. Write a program to input two numbers(A & B) from user and print the maximum element among A & B in each line.

Solution(1):

  firstNumber = int(input())
  secondNumber = int(input())

  if firstNumber>secondNumber:
    print(firstNumber)
  else:
    print(secondNumber)
     
"""


"""
2. Write a program to input a number(A) from user and print 1 if it is positive, -1 if it is negative, 0 if it's neither positive nor negative.


Solution(2):

  userNumber = int(input())
  if userNumber == 0:
    print(0)
  elif userNumber > 0:
    print(1)
  else:
    print(-1)

"""


"""
3. Write a program to input an integer from user and print 1 if it is odd otherwise print 0.

Solution(3):

  userNumber = int(input())
  if userNumber%2 == 0:
    print(0)
  else:
    print(1)

"""


""" 

4. Write a program to input an integer(A) from user and print the Ath month of the year.

Months list: {January, February, March, April, May, June, July, August, September, October, November, December}
  
  
Solution(4):

userInput = int(input())
if userInput == 1:
    print("January")
elif userInput == 2:
    print("February")
elif userInput == 3:
    print("March")
elif userInput == 4:
    print("April")
elif userInput == 5:
    print("May")
elif userInput == 6:
    print("June")
elif userInput == 7:
    print("July")
elif userInput == 8:
    print("August")
elif userInput == 9:
    print("September")
elif userInput == 10:
    print("October")
elif userInput == 11:
    print("November")
else:
    print("December")


"""



"""
5. Print the result of the following expression:

(3 + 4) // 2 + 6

Solution(5):
  print(9)

"""


"""
6. Set the value of variable a, b and c such that the following condition evaluates to true:

a = -1 # change this
b = -1 # change this
c = -1 # change this

# DO NOT CHANGE THIS
x = a < b + c

print(x) # this should be True



Solution (6):

a = 1
b = 1
c = 1
x=50
x = a < b + c
print(x)

"""



"""
7. You are given 3 integer angles(in degrees) A, B and C of a triangle. You have to tell whether the triangle is valid or not.

A triangle is valid if sum of its angles equals to 180

Solution(7):
    firstAngle = int(input())
    secondAngle = int(input())
    thirdAngle = int(input())

    if firstAngle+secondAngle+thirdAngle == 180:
        print(1)
    else:
        print(0)
        
"""



"""
8. Write a program to input two numbers(A & B) from user and print the minimum element among A & B in each line.


Solution(8):

firstNumber = int(input())
secondNumber = int(input())

if firstNumber > secondNumber:
    print(secondNumber)
else:
    print(firstNumber)

"""


"""
Q9. You are given the Cost Price C and Selling Price S of a Product. You have to tell whether there is a Profit or Loss. Also, calculate total profit or loss.

NOTE: It is guaranteed that Cost Price and Selling Price are not equal.


Solution(9):
costPrice = int(input())
sellingPrice = int(input())

if costPrice<sellingPrice:
    print(1)
    print(sellingPrice-costPrice)
else:
    print(-1)
    print(costPrice-sellingPrice)
"""



"""
10. Write a program to input from user an integer(A) representing the rating of a person on a platform.

You have to print the category of that person.
If the rating is greater than or equal to 2100 then that person is "grand master".
If the rating is greater than or equal to 1900 then that person is "candidate master".
If the rating is greater than or equal to 1600 then that person is "expert".
If the rating is greater than or equal to 1400 then that person is "pupil".
If the rating is smaller than 1400 then that person is "newbie".
NOTE: Print all the chars of the category of the person in lowercase if rating is odd otherwise print in UPPERCASE


Solution(10):

userRating = int(input())

if userRating >= 2100:
    if userRating%2 == 0:
        print("grand master".upper()) 
    else :
        print("grand master".lower())
elif userRating >= 1900:
    if userRating%2 == 0:
        print("candidate master".upper()) 
    else:
        print("candidate master".lower())
elif userRating >= 1600:
    if userRating%2 == 0: 
        print("expert".upper()) 
    else:
        print("expert".lower())
elif userRating >=1400:
    if userRating%2 == 0:
        print("pupil".upper()) 
    else:
        print("pupil".lower())
else:
    if userRating%2 == 0: 
        print("newbie".upper()) 
    else:
        print("newbie".lower())

"""







