import random
from word import word_list

def get_words():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 7
    print("Play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please try a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters():
                print("You already guessed that letter", guess)
            elif guess not in word:
                print(guess, "Is not in that word.")
                tries -= 1
                guessed_letters.append(guess)
            else    

