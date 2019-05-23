# Notice:
# On the 3rd trial when the Computer Player plays against another Computer Player, it outputs like an infinite loop, but
# it eventually gets to a winner like a regular Human vs Human game

import random

class Player():
    def getGuess():
        raise NotImplementedError 

class HumanPlayer(Player):

    def __init__(self):
        pass

    def getGuess(self):
        Yes = True
        #num = input("Enter a guess from 0 to 99: ")
        while Yes:
            try:
                num = input("Enter a guess from 0 to 99: ")
                if type(eval(num)) != int:
                    print("Invalid value entered:",str(num),'try again')
                    Yes = True
                elif type(eval(num)) == int:
                    if ((int(num) >= 0) and (int(num) <= 99)):
                        Yes = False
                        return int(num)
                    else:
                        raise
                        
                
            except :
                print('Invalid value entered:',str(num),'try again')
                #num = input("Enter a guess from 0 to 99: ")
                Yes = True
        
class ComputerPlayer(Player):

    def __init__(self):
        pass

    def getGuess(self):
        return random.randint(0,99)

def checkForWin(guess,answer):
    print("You guessed ", str(guess), ".")
    if (answer == guess):
        print("You're right! You win!")
        return True;
    elif (answer < guess):
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
        return False;
    # end definition of checkForWin function

def play(player1, player2, answer):  #(obj1,obj2,integer)
    guess = 0
    win = False

    while (not win):
        print("Player 1's turn to guess.")
        guess = player1.getGuess()
        win = checkForWin(guess, answer)
        if (win):
            return
        print("Player 2's turn to guess.")
        guess = player2.getGuess()
        win = checkForWin(guess, answer)
    #end definition of play function



#MAIN
# Calls function play with 2 object instances of HumanPlayer
# Calls function play with 2 object instances of HumanPlayer and ComputerPlayer
# Calls function play with 2 object instances of ComputerPlayer
print('Human vs Human game')
ans = random.randint(0,99) #HvH
hum1 = HumanPlayer()
hum2 = HumanPlayer()
play(hum1,hum2,ans)
print('\n')

print('Human vs Computer Player')
ans2 = random.randint(0,99) #HvC
hum3 = HumanPlayer()
Comp1 = ComputerPlayer()
play(hum3,Comp1,ans2)
print('\n')

print('Computer vs Computer')
ans3 = random.randint(0,99) #CvC
Comp2 = ComputerPlayer()
Comp3 = ComputerPlayer()
play(Comp2,Comp3,ans3)
