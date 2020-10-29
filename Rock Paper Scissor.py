import random
from random import randint

print("Winning Rules for this Game: \n"
							+ "Rock Vs Paper -> Paper Wins \n"
							+ "Rock Vs Scissor -> Rock Wins \n"
							+ "Paper Vs Scissor -> Scissor Wins \n")

list0 = ["Rock", "Paper", "Scissors"]


robot = list0[randint(0,2)]

Round = 5
R = 0
Z = 0

for i in range(Round):
    zack = input("Enter Your Choice from Rock, Paper, Scissors \n")
    if zack == robot:
        print("Tie!!!")
        R = R + 0
        Z = Z + 0
    elif zack == "Rock":
        if robot == "Paper":
            print("You lose!!!")
            R = R + 1
        else:
            print("You win!!!")
            Z = Z + 1
    elif zack == "Paper":
        if robot == "Scissors":
            print("You lose!!!")
            R = R + 1
        else:
            print("You Win!!!")
            Z = Z + 1
    elif zack == "Scissors":
        if robot == "Rock":
            print("You lose!!!")
            R = R + 1
        else:
            print("You Win!!!")
            Z = Z + 1
    else:
        print("That's not a valid input. Try again with correct word!")
    robot = list0[randint(0, 2)]

if Z > R:
    print("Final Result: Congratulations!! You Win the Round!!!")
elif Z == R:
    print("Final Result: !! Round ended with Tie !!!")
else:
    print("Final Result: Sorry!!! You lose the Round !!!")