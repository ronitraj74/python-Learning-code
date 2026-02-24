'''
name = input("Enter your name here : ")
def goodday(name,ending):
    print("hiiiii, good morning " + name)
    print(ending)
    return "done"
output = goodday(name, "Thank you")
print(output)
'''
#-----------------------average of three number -------------------------------
'''
def average(ending):
    a = int(input("Enter the first number : "))
    b = int(input("Enetr the second number : "))
    c = int(input("Enter the third number : "))
    print((a+b+c)/3)
    print(ending)
average("Thank you")
average("Thank you")
'''
#-----------------------default parmeter value----------------------------------
'''
# def goodDay(name,ending = "Thanks"):
#     print(f"Hiiiiiiiiiiii {name}")
#     print(ending)
# goodDay("Ronit","Thank you")
'''
#-----------------------Recursion----------------------------------------------
'''
n = int(input("Enter the number to find factorial : "))
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)
print(f"the factorial of the given number is: {factorial(n)}")
'''
