# n = int(input("Enter the number to print table :"))
# for i in range(1,11):
#     {
#     print(f"{n} * {i} = {n*i}")
# }
# -------------------------------------------------------------------------------------
# l = ["Harry", "Ronit" , "Sahil", "soham", "Sachine"]
# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello {name}")
# -------------------------------------------------------------------------------------
# n = int(input("Enter the number to print table :"))
# i = 1
# while i <= 10:
#     print(f"{n} * {i} = {n*i}")
#     i += 1
# #-----------------------------------------------------------------------------------
# num = int(input("Enter any number to cheack it is prime or not : "))
# for i in range (2,num ):
#     if(num % i) == 0:
#         print("Number is not prime ")
#         break
# else:
#         print("Number is prime")
# --------------------------------------------------------------------------------------
# num = int(input("Enter the number to print sum : "))
# i = 1
# sum = 0
# while(i<=num):
#         sum += i
#         i += 1
# print(sum)
# --------------------------------------------------------------------------------------
# ----------------------factorial using while loop--------------------------------------
# num = int(input("Enter the number to find factorial : "))
# i = 1
# factorial = 1
# while(i<=num):
#     factorial *= i
#     i +=1
# print(factorial)
# --------------------------------------------------------------------------------------
# ----------------------factorial using for loop--------------------------------------
# num = int(input("Enter the number to find factorial :"))
# fact = 1
# for i in range(1 , num+1):
#     fact = fact * i

# print(f"factorial of number {num} is {fact}")
# --------------------------------------------------------------------------------------
'''
Docstring for 07_07question
    *
   * *
  * * *

# r = int(input("Enter the number of rows to print star pyramid : "))
# for i in range(1,r+1):
#     print(" "*(r-i),end=" ")
#     print("*"*(2*i-1),end=" ")  
#     print("\n")

'''
'''
*
* *
* * *
* * * *
'''
# r = int(input("Enter the number of rows :"))
# for i in range(1,r+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# r = int(input("Enter the number of the rows : "))
# for i in range(1,r+1):
#     print("*"*i)
#     print("")

'''
* * * 
*   *
* * *   n = 3
'''

# n = int(input("Enter the number of rows : "))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#       print("*"*n,end="")
#     else:
#        print("*",end="")
#        print(" "*(n-2),end="")
#        print("*",end="")
#     print()
# -----------------multiplication table in reversed order-------------------------------
# n = int(input("Enetr the number to print its table in reverse order : "))
# for i in range(1,11):
#     print(f"{n}*{11-i}={n*(11-i)}")
