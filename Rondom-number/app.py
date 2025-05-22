#number guesing game

import random 

target= random.randint(1,100)

while True:
    userChoice = int(input("Guess the target Or Qiut :"))
    if(userChoice == "Quit"):
        break
    userChoice =int(userChoice) 
    if(userChoice == target):
        print("Sucess : Correct Guess!!")
        break
    elif(userChoice < target):
        print("Your number was too small. Take a bigger guess....")
    else:
        print("Your number was too big. Take a small guess....")
print("____GAME OVER____")































