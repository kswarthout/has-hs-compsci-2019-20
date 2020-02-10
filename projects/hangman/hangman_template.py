# Name:

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

# Methods to Implement
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    ####### Pseudocode ##########
##    Start with an empty string.
##    
##    Loop over the characters in secret word.
##
##    If the letter is not in letters
##    guessed, return false, as it indicates
##    not all letters have been guessed yet
    #############################
    
    ####### YOUR CODE HERE ######
    pass # This tells your code to skip this function; delete it when you
         # start working on this function


def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    global secret_word
    global letters_guessed

        ####### Pseudocode ##########
##    Start with an empty string.
##    
##    Loop over the characters in secret word.
##
##    If the letter is in the letters_guessed list,
##    append that letter to the end of your empty string,
##    otherwise, append a '-' character
##
##    Print the string you built after the secret_word
##    loop completes.
    #############################
    
    ####### YOUR CODE HERE ######
    pass # This tells your code to skip this function; delete it when you
         # start working on this function

def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0
    ####### Pseudocode ##########
##    Game play continues until 6 mistakes are made.
##    Use a loop that will execute until this condition
##    is met.

##    Inside the game loop, print to the
##    console how many guesses are left.
##    Then, print the letters guessed using the
##    print_guessed() function.
##
##    Get input from the user representing their guess.
##
##    If the letter is already in letters_guessed,
##    do not add it to the list.
##
##    If the word is guessed, terminate the
##    game loop by satisfying the terminating condition
##
##    If the guess is not in the secret_word,
##    add 1 to the mistakes_made variable.
##
##    After the game loop, indicate to the
##    user whether or not they have won,
##    and print the secret_word to the console
    
    #############################
    

    # Update secret_word. Don't uncomment this line until you get to Step 8.
    # secret_word  = get_word()

    ####### YOUR CODE HERE ######
    return None

    
