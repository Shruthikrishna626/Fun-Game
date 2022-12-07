#Rock ,Paper , Scissor
#Let's have some FUN

from random import randint

options=["Rock","Paper","Scissor"]
computer=options[randint(0,2)]
player=False
trys=5
point=0
print("Game Starts!!!Go!")
while player==False and trys>=1:
    player=input("Rock ,Paper,Scissor???\n")
    if player==computer:
        print("OOps!Tie!!!")
    elif player=="Rock":
        if computer=="Paper":
            print("You Lose!",computer ,"covers",player)
        else:
            print("You Win!",player,"smashes",computer)
            point=point+1
            print("You earned 1 point")
        trys=trys-1
        if trys>0:
            print("Now",trys,"tries left!")
        else:
            print("Game Over!")
    elif player=="Scissor":
        if computer=="Paper":
            print("You Win!",player,"cuts",computer)
            point=point+1
            print("You earned 1 point")
        else:
            print("You Lose!",computer,"smashes",player)
        trys=trys-1
        if trys>0:
            print("Now",trys,"tries left!")
        else:
            print("Game Over!")
    elif player=="Paper":
        if computer=="Scissor":
            print("You Lose!",computer,"cuts",player)
        else:
            print("You Win",player,"covers",computer)
            point=point+1
            print("You earned 1 point")
        trys=trys-1
        if trys>0:
            print("Now",trys,"tries left!")
        else:
            print("Game Over!")
    else:
        print("Invalid Choice!or Check your spelling")
    player=False
    computer=options[randint(0,2)]
if point<3:
    print("Your,point is",point,"out of",trys,"Better luck next Time!")
else:
    print("Congratulations!You have earned",point,"points!")
