import random

def throw():
    list1 = ['rock', 'paper', 'scissors']
    return random.choice(list1)

players = 2
total_players_scores = []
for _ in range(2):
    total_players_scores.append(0) # [0, 0]
max_score = 2
# we have to ask player number 1 and 2 to throw
# after both has thrown, we have to print what throws were at the same time

while max(total_players_scores) <= max_score:
    thrown = [] # in this list we will append the throws
    for pi in range(players):
        thrown.append(throw())

    if thrown[0] == 'rock' and thrown[1] == 'paper':
        print(f'Player 1 threw', thrown[0].upper(), 'and Player 2 threw', thrown[1].upper())
        print('Player 2 wins.')
        total_players_scores[1] += 1

    elif thrown[0] == 'rock' and thrown[1] == 'scissors':
        print(f'Player 1 threw', thrown[0].upper(), 'and Player 2 threw', thrown[1].upper())
        print('Player 1 wins.')
        total_players_scores[0] += 1

    elif thrown[0] == 'paper' and thrown[1] == 'scissors':
        print(f'Player 1 threw', thrown[0].upper(), 'and Player 2 threw', thrown[1].upper())
        print('Player 2 wins.')
        total_players_scores[1] += 1

    elif thrown[0] == 'paper' and thrown[1] == 'rock':
        print(f'Player 1 threw', thrown[0].upper(), 'and Player 2 threw', thrown[1].upper())
        print('Player 1 wins.')
        total_players_scores[0] += 1

    elif thrown[0] == 'scissors' and thrown[1] == 'rock':
        print(f'Player 1 threw', thrown[0].upper(), 'and Player 2 threw', thrown[1].upper())
        print('Player 2 wins.')
        total_players_scores[1] += 1

    elif thrown[0] == 'scissors' and thrown[1] == 'paper':
        print(f'Player 1 threw', thrown[0].upper(), 'and Player 2 threw', thrown[1].upper())
        print('Player 1 wins.')
        total_players_scores[0] += 1

    elif thrown[0] == thrown[1]:
        print(f'Player 1 threw', thrown[0].upper(), 'and Player 2 threw', thrown[1].upper())
        print('Try again.')

    if max(total_players_scores) == 2:
        break

print('\nThe total score is', total_players_scores)

winning_score = max(total_players_scores)

winner = total_players_scores.index(winning_score)

print('\nThe winner is Player', winner+1,'!!!')