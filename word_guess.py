"""
File: word_guess.py
-------------------
This word guessing game prompts the user to guess letters in a secret word. The secret word is randomly selected from
a file. The user can quit at anytime by typing 0. Once the user wins or loses, they can choose to play again or quit.
"""


import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    """
    This function plays the main game when given a secret word. The
    'letters' list keeps track of the correct letters the user has
    entered and their positions relative to the secret word. The
    correct_letters list contains each letter of the secret word
    in order and is used to check the user's guess.
    """
    while True:
        guesses = INITIAL_GUESSES
        letters = []
        correct_letters = list(secret_word)
        guess = ''

        for elem in secret_word:
            letters.append('-')

        word = "".join(letters)
        show_word(word)
        show_guesses(guesses)

        # main game: while-loop runs until the user guesses the word, runs out of guesses, or types 0
        while guesses != 0:
            guess = input('Type a single letter here, then press enter (Enter 0 to quit) ').upper()
            if guess == '0':
                break
            elif len(guess) != 1:
                pass
            else:                                                          # main program logic
                if guess in correct_letters:                               # if guess is correct:
                    print('That guess is correct')
                    for i in range(len(secret_word)):                      # finds position of guess in secret word
                        if letters[i] == '-' and guess == secret_word[i]:  # checks if first time guessed
                            letters.pop(i)                                 # removes '-'
                            letters.insert(i, guess)                       # insert the correct letter guessed
                            word = "".join(letters)                        # create word string from letters list
                    if word == secret_word:                                # breaks out of loop if secret word is found
                        break
                    show_word(word)
                else:
                    print(f"There are no {guess}'s in the word")           # if guess is not correct:
                    guesses -= 1                                           # reduce guesses available by 1
                    show_guesses(guesses)
                    show_word(word)

        # determines if the user won, lost, or quit and prints the corresponding message
        if guesses == 0:
            print(f'Sorry, you lost. The secret word was: {secret_word}')
        elif guess == '0':
            break
        else:
            print(f'Congratulations, the word is: {secret_word}')

        # asks the user if they want to play again, if they enter 'y', the game restarts, otherwise the game ends
        play_again = input("Would you like to play again? (enter y to play again, type anything else to quit) ").lower()
        if play_again == 'y':
            secret_word = get_word()
            pass
        else:
            break

    print('Thanks for playing!')


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    word_list = []
    with open(LEXICON_FILE) as file:
        for line in file:
            line = line.strip()
            word_list.append(line)

    index = random.randint(0, len(word_list))

    return word_list[index]


def show_word(word):
    """
    This function displays the current word based on user guesses.
    """
    print(f'The word now looks like this {word}')


def show_guesses(guesses):
    """
    This function displays the number of guesses the user has left.
    """
    print(f'You have {guesses} guesses left')


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()