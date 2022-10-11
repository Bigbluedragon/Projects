# rock, paper and scissors AI game
from random import randint

# moves for the player
moves = ['rock', 'paper', 'scissors']

while True:
    computer = moves[randint(0,2)]
    player = input("rock, paper or scissors? (or end?)").lower()
    if player == 'end':
        print('The game has ended')
        break
    elif player == computer:
        print('It is a . . . tie')
    elif player == "rock":
        if computer == "paper":
            print("You . . . Lost :(")
        if computer == "scissors":
            print("You . . . WON")
    elif player == "paper":
        if computer == "scissors":
            print("You . . . Lost :(")
        if computer == "rock":
            print("You . . . WON")    
    elif player == "scissors":
        if computer == "rock":
            print("You . . . Lost :(")
        if computer == "paper":
            print("You . . . WON")            
    else:
        print('Check your spelling . . .')
