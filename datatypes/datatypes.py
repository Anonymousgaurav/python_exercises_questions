
# 1. Given two numbers A and B. Concatenate the two numbers and print it.

"""
Solution (1).

a, b = int(input()), int(input())
print(str(a) + str(b))

"""

"""
2. Your friend Rahul plans to visit exotic countries all around the world. Sadly, Rahul's math skills aren't good.
He's pretty worried about being scammed by currency exchanges during his trip - and he wants you to make a currency
calculator for him. Here are his specifications for the app:
Given the amount of money before exchange and the amount of money that is taken from the budget to be exchanged,
print the amount of money that is left from the budget.

Input Format

First line contains an integer N denoting the total budget, amount of money before exchange.
Second line contains an integer M denoting the exchanging amount, denoting the amount of money that is taken from the budget to be exchanged.

Output Format

Print a single line denoting the amount of money that is left from the budget.

Solution (2):

    a = int(input())
    b = int(input())

    print(a-b)

"""

"""
3. Your friend Rahul plans to visit exotic countries all around the world. Sadly, Rahul's math skills aren't good.
He's pretty worried about being scammed by currency exchanges during his trip - and he wants you to make a currency
calculator for him. Here are his specifications for the app:

Given the total budget and the value of a single bill, your need to print the no of new currency bills that you can receive 
within the given budget.
In other words: How many whole bills of new currency fit into the amount of old currency you have in your budget?
Remember -- you can only receive whole bills, not fractions of bills, so remember to divide accordingly. Effectively, you are rounding down to the nearest whole bill/denomination.

Input Format

First line contains an real number N denoting the total budget.
Second line contains an integer M denoting the value of a single bill.

Output Format
Print in a single line denoting the total numbers of bills which should be an integer.


Solution(3) : 

    a = float(input())
    b = int(input())

    print(round(a/b))

"""

"""
4. Your friend Rahul plans to visit exotic countries all around the world. Sadly, Rahul's math skills aren't good. He's pretty worried about being scammed by currency exchanges during his trip - and he wants you to make a currency calculator for him. Here are his specifications for the app:

Given the value of a single bill and the amount of bills you received, print the total value of the bills.

Input Format
The first line of the input is an integer N denoting the value of a single bill.
The second line of the input is an integer M denoting the number of bills.

Output Format
Print in a single line denoting the total value of bills.

Solution(4):
    
    N = int(input())
    M= int(input())
    print(N*M)

"""

"""
5. Given two names A and B as input. Print "A says Hi to B". where A and B are the names in input.

Solution(5):
    a = str(input())
    b = str(input())
    print(a +" says Hi to "+ b)

"""


"""
6. Given a name A as input. Print "Hello A", where A is the name in input.

Solution(6):
    A = input()
    print("Hello "+A)

"""


"""
7. Print the first five letters of the English alphabet i.e. A, B, C, D and E.
    print("A","B","C","D","E",sep="\n")
    
"""


"""
8. You're going to write some code to help you cook a gorgeous lasagna from your favorite cookbook.
According to your cookbook, the Lasagna should be in the oven for 40 minutes:
Given the actual minutes the lasagna has been in the oven, find how many minutes the lasagna still needs to bake.
Input Format

The only first line contains the integer N denoting the actual minutes the lasagna has been in the oven.

Output Format

Print in a single line how many minutes the lasagna still needs to bake.


Solution(8):
    lasagnaTime = 40
    remainingTime  = int(input())
    print(lasagnaTime-remainingTime)

"""


"""
9. You're going to write some code to help you cook a gorgeous lasagna from your favorite cookbook.
Now, you want to also add few layers to the lasagna. Assume each layer takes 2 minutes to prepare.
Given the number of layers you want to add to the lasagna, find how many minutes you would spend making them.

Input Format
The only first line contains the integer N denoting the number of layers.

Output Format
Print in a single line how many minutes are required to prepare N layers.

Solution(9):
    
    preparationTime = 2
    layers = int(input())
    print(preparationTime*layers)

"""

"""
10. You're going to write some code to help you cook a gorgeous lasagna from your favourite cookbook.
Now, you want to find the total number of minutes you've been cooking or the sum of your preparation time and the time the lasagna has already spent baking in the oven. The preparation time of one layer is 2 minutes.

Given the number of layers added to the lasagna and the number of minutes the lasagna has been baking in the oven, find the total elapsed cooking time (prep + bake) in minutes.

Input Format
Their are 2 lines in the input.
The first line contains the integer N denoting the number of layers.
The second line contains the integer M denoting the time the lasagna has already spent baking in the oven.

Output Format
Print in a single line the total elapsed cooking time.

Solution(10):
    preparationTime = 2
    numOfLayers = int(input())
    layerPreparing = int(input())
    print(preparationTime*numOfLayers+layerPreparing)
"""

