import random

def rps():

#User Choice + make sure its a valid anwser if it isnt then they dum
    userchoice = input("Choose one, Rock/Paper/Scisors").lower().title().strip()


        
#Get the bots decision
    botchoice = random.choice(["Rock", "Paper", "Scisors"]) 

#decide winner timeeee
    if userchoice == botchoice:
        print("L u tied against bot")

    elif (   (userchoice == 'Rock' and botchoice == 'Scisors')or
    (userchoice == 'Paper' and botchoice == 'Rock')or
    (userchoice == 'Scisors' and botchoice == 'Paper')
    ):    
        print("U WIN")
    
    else:
        print("L BOZO")

rps()








