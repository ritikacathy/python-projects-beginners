import random

def roll():
    minimum = 1
    maximum = 6
    rolls = random.randint(minimum, maximum)
    return rolls

while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break # breaks out of the endless while loop
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
players_total_score = []
for _ in range(players): # if 2 players are playing
    players_total_score.append(0)
print('The current scores are', players_total_score)


while max(players_total_score) <= max_score:
    for pi in range(players): # if 2 players are playing, pi will be 0, 1

        print('It is your turn, Player', pi+1)
        player_score = 0
        while True:
            decision = input('Would like to play (y)?: ')
            if decision.lower() != 'y': # if the decision is not a yes

                break # that player's turn is over and final score is taken

            rolled = roll() # if the player decides to play

            print('You rolled:', rolled)
            if rolled == 1:
                print('You rolled a 1! Turn over.')
                player_score = 0
                break
            else: # if we do not get a 1

                player_score += rolled # scores are accumilated 

            print('Your current score is', player_score)
        players_total_score[pi] += player_score # when the game is over either player stops playing or gets 1

        print('Your total score is', players_total_score[pi])

# get the index in this list whose value is the max

winning_score = max(players_total_score)
winner = players_total_score.index(winning_score)
print('Player', winner+1, 'is the winner with a total score of', winning_score, '!!!!')

            

