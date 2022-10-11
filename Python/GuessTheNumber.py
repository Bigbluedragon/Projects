from random import randint

random_number = randint(1, 10)
player_points = 0

print('--- Guess The Number ---')
while True:
    number = input('What do you think the number is 1-10?' "\n" 'Type quit to end the game' "\n")

    if number == 'quit':
        print('--- LeaderBoard --- \n You - Score', str(player_points))
        quit()

    elif number == str(random_number):
        print('You guessed the number!')
        player_points += 10
        random_number = randint(1, 10)
        
    else:
        print('You didn\'t guess the number \n' 'Have another go! \n')
        player_points -= 2
        



   
