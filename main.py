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
