import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # Chooses random word from list
    
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = list(word) # initialize all letters in a word
    alphabets = set(string.ascii_uppercase) # initialize all english alphabets in upper case
    used_letters = set() # initialize all guessed letters

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # used letters:
        print('You have used these letters: ', ' '.join(used_letters))

        # current word (i.e: W _ R _ )
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))
        print(f'{len(word_letters)} letters left of {len(word_list)} letters word and you have {lives} Lives left.')

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1 # takes away a life if wrong
                print('letter is not in word')
        elif user_letter in used_letters:
            print('You have already used this character, Please try again.')
        else:
            print('Invalid Character, Please try again.')
    
    # Reached there if len(word_letters) == 0 and lives == 0
    if lives == 0:
        print(f'You died, sorry. The word was {word}')
    else:
        print(f'You guessed the word {word}!')

hangman()
