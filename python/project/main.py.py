'''
Docstring for projrct.01_project
Here,
    1 = snake
    2 = Water 
    3 = gun
'''
import random
computer = random.choice([1,2,3])
print("s for snake, \nw for Water \ng for gun")
youstr = input("Enter your choice : ")
youDict = {"s" : 1, "w" : 2, "g" : 3}
reverseDict = {1 : "snake", 2 : "water" , 3 : "gun"}

you = youDict[youstr]
print(f"you Choose {reverseDict[you]} \n and Computer Choose {reverseDict[computer]}")
if (computer == you):
    print("Game is Draw :) ")
else:
    if(computer == 2 and you == 1):
        print("You win!")
    elif(computer == 2 and you == 3):
        print("You lose!")
    elif(computer == 1 and you == 2):
        print("You lose!")
    elif(computer == 1 and you == 3):
        print("You Win!")
    elif(computer == 3 and you == 2):
        print("You Win!")
    elif(computer == 3 and you == 1):
        print("You lose!")
    else:
        print("Somethings went worng")