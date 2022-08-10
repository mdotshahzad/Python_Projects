import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in words or '' in words:
        word = random.choice(words)
    return word



def hangman():
    word  = get_valid_word(words)
    print(word)
    word_letter = set(word) #letter in the word
    alphabet = set(string.ascii_uppercase)

    used_letter = set() #what the user has guessed
    #user inout 
    while len(word_letter) > 0:
        print('Alreay used letter ', ' '.join(used_letter))

        #what is current word
        word_list = [letter if letter in used_letter else '-' for letter in word]
        print('Current Word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
        elif user_letter in used_letter:
            print("Already used. Try Again") 

        else:
            print("Invalid Char: Try Again")       




hangman()