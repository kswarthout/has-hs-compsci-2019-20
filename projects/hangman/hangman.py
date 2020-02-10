# Name: Kari Swarthout

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    # wordlist = split(line)
    wordlist = line.split()
    print ("  ", len(wordlist), "words loaded.")
    print ('Enter play_hangman() to play a game of hangman!')
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = 'claptrap' 
letters_guessed = []

def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    for letter in secret_word:
        if letter not in letters_guessed:
            return False
            
    return True


def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    global secret_word
    global letters_guessed

    guessed = ''
    for letter in secret_word:
        if letter in letters_guessed:
            guessed += letter
        else:
            guessed += '-'

    print(guessed)


def play_hangman():
    global secret_word
    global letters_guessed
    mistakes_made = 0

    # Update secret_word. Don't uncomment this line until you get to Step 8.
    # secret_word  = get_word()

    while mistakes_made < MAX_GUESSES:
        print(str(MAX_GUESSES - mistakes_made) + ' guesses left')
        print_guessed()

        guess = input('Guess a letter: ').lower()
        
        if guess not in letters_guessed:
            letters_guessed.append(guess)

        if word_guessed():
            mistakes_made = 6
            print('You win!')

        if guess not in secret_word:
            mistakes_made +=1

    
