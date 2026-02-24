#----------------write a python program to print high score from computer and print hi-score in new text file-----------------
import random
def game():
    print("You are playing game.........")
    score = random.randint(1,100)
    #fetch the hi-score
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
                
    print(f"Your score is : {score}")
    if(score>hiscore):
        with open("hiscore.txt","w") as f:
            f.write(str(score))
    
    return score

game()

