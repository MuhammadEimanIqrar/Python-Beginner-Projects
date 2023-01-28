import random

def guess(x: int) -> str:
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # it could also be high b/c at this point low = high
        feedback = input(f'In {guess} is too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number {guess}, correctly!')

guess(1000)
