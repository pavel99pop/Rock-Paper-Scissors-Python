import random

user_score = 0
computer_score = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input('\nType Rock/Paper/Scissors or Q to quit: ').lower()

    if user_input == 'q':
        break

    if user_input not in options:
        continue

    random_number = random.randrange(3)
    computer_input = options[random_number]
    print('Computer chose ' + computer_input)

    if user_input == computer_input:
        print('Tie!')
        continue

    if user_input == 'rock' and computer_input == 'scissors':
        print('You win!')
        user_score += 1
    elif user_input == 'paper' and computer_input == 'rock':
        print('You win!')
        user_score += 1
    elif user_input == 'scissors' and computer_input == 'paper':
        print('You win!')
        user_score += 1
    else:
        print('Computer wins!')
        computer_score += 1

print('Your score: ', user_score)
print('Computer score: ', computer_score)