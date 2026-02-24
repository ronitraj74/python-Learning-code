# # print("hello world")
# print("Ronit")
#------------------------------------------------------------------------------------------------
# a = int(input("Enter the number : "))
# if(a>20):
#     print("Number is greater than 20")
# elif(a == 20):
#     print("Number is 20")
# else: 
#     print("number is lesser")
#------------------------------------------------------------------------------------------------
# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the second number : "))
# num3 = int(input("Enter the third number : "))
# num4 = int(input("Enter the third number : "))
# if(num1>num2 and num1>num3 and num1>num4):
#     print("The largest number is ",num1)
# elif(num2>num1 and num2>num3 and num2>num4):
#     print("The largest number is ", num2)
# elif(num3>num1 and num3>num2 and num3>num4):
#     print("The largest number is ", num3)
# else:
#     print("The largest number is ", num4)
#------------------------------------------------------------------------------------------------
maths = int(input("Enter the number in maths : "))
dsa = int(input("Enter the number in DSA : "))
oops = int(input("Enter the number in OOPS : "))
dcca  = int(input("Enter the number in DCCA : "))
toc = int(input("Enter the number in TOC : "))
total_percentage = (maths+dsa+oops+dcca+toc)/5
if(total_percentage >= 40):
    print("PASS")
else:
    print("FAIL")
#------------------------------------------------------------------------------------------------