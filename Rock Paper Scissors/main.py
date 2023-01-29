import random

def play():
    choices = {
        'r': 'Rock',
        'p': 'Paper',
        's': 'Scissor'
    }
    user = input("What's your choice? 'r' for Rock, 'p' for Paper, and 's' for Scissors \n").lower()
    choiceKeys = list(choices.keys())
    computer = random.choice(choiceKeys)

    if not user in choiceKeys:
        print(f'{user} is not a valid choice')

    if user == computer:
        print('It\'s a tie')
    
    # r > s, s > p, p > r
    if is_win(user, computer):
        print(f'You Won Computer Choosed: {choices[computer]}')
    elif is_win(computer, user):
        print(f'You Lost Computer Choosed: {choices[computer]}')
    
    playAgain = input("Do you want to play again? If yes enter 'y', if no enter 'n': ")
    if playAgain == 'y':
        play()
    else:
        print('Thank You!')

def is_win(user, computer):
    # Return True if player wins
    # r > s, s > p, p > r
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True

play()
