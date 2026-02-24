#-----------Write a program using function to find the greatest of the three number----------
'''
def greatest(ending = "Thanking you!"):
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number :"))
    num3 = int(input("Enter the third number : "))
    if(num1>num2 and num1>num3):
        print(f"Greatest number is : {num1}")
    elif(num2>num1 and num2>num3):
        print(f"Greatest number is : {num2}")
    else:
        print(f"Greatest number is : {num3}")
    print(ending)
        
greatest()
greatest()
greatest()
'''
#-----------------------write a program to convert celsius into fahrenheit---------------------
'''
def celsius():
    cel = int(input("Enter the celsius tempreture to convert it into fahrenheit : "))
    fahr = (cel * (9/5))+32
    print(f"The given tempreture in fahrenheit is : {fahr}")
celsius()
'''
#---------------------How do you prevent a python print() function to print a new line at the end--------------
#use end keyword
"""
print("a")
print("b")
print("c")
print("d")
print("e")
print("f",end="")
print("g",end="")
print("h",end="")
print("i",end="")
print("j",end="")
print("k",end="")
print("l",end="")
"""
#--------------------Write a recursive function to calculate the sum of first n natural number--------------------
'''
num = int(input("Enter the n natural number to find its summation : "))
def sum(num):
    if(num==1):
        return 1
    return sum(num-1) + num
print(sum(num))
'''
#---------------------Write a program to print first n line of the following pattern----------------------
'''
***
**
*
'''
'''
n = int(input("Enter the number of rows to print pattern : "))
def pattern(n):
    if(n == 0):
        print("-------Nothing to be print here-------")
        return
    print("*" * n)
    pattern(n-1)
pattern(n)
'''
#---------------Write a program to convert inches into centi mertre---------------------------------
"""
n = int(input("Write mesurement in inches to convert it into centimetre : "))
def converter():
    if(n == 0):
        return 0
    cm = n * 2.54
    print(f"the given mesurement is in cm is {cm}")

converter()
"""
#-----------------Write a program to print a multiplication table of the given number------------------------------
'''
n = int(input("Enter the number to print a multiplication table : "))
def table(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")

table(n)
'''