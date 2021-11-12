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
            else:
                print("Great job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list) 
                if "_" not in word_completion:
                    guessed = True   

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You have already guessed that word", guess)
            elif guess != word:
                print(guess, "Incorrect word")  
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word    
        else:  
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n") 
    if guessed:
        print("Congrats, you guessed the word! You Win!")
    else:
        print("Oh no, looks like you've ran out of tries. The word was " + word ". Better luck next time")    

def main():
    word = get_words()
    play(word)
    while input("Play again? (Y/N) ").upper() == "Y":
        word = get_words()
        play(word)

if __name__ == "__main__":
    main()