# Hangman

We’re going to write the game of Hangman. This document provides a step-by-step approach to help you build the game. Use it as much or as little as you want. If you’re uncertain, I recommend sticking with the document; however, if you want to try attacking this program on your own, that’s great too. 

## Problem Description:

Download the file [hangman_template.py](https://github.com/kswarthout/has-hs-compsci-2019-20/blob/master/projects/hangman/hangman_template.py) and save it as hangman.py. 
Also download [words.txt](https://github.com/kswarthout/has-hs-compsci-2019-20/blob/master/projects/hangman/words.txt) and save it in the same place.

We’re going to start by storing the state of the game in variables at the top of the function `play_hangman`. The state is a complete description of all the information about the game.  

For Hangman, we need to store 3 pieces of information:
- `secret_word`: The word they are trying to guess (string).
- `letters_guessed`: The letters that they have guessed so far (list).
- `mistakes_made`: The number of incorrect guesses they’ve made so far (int).

You can name these something else if you’d like, but use a descriptive name. For now, set secret word to be “claptrap”.

Once we’ve finished our program and got it working, then we’ll change the secret word = ’claptrap’ to be `get_word()`, a function that pulls a random word from the file words.txt. This function is already defined for you. (This is called incremental programming - instead of trying to get everything right the first time, we’ll get the basic program working then incrementally add small portions of code.) “claptrap” was selected because it’s reasonably long and has duplicate letters – hopefully that will allow us to catch any bugs we might make.

This project was adapted from MIT OpenCourseWare 6.189 [Hangman Project](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-a-gentle-introduction-to-programming-using-python-january-iap-2011/assignments/MIT6_189IAP11_project1.pdf)

## Here’s our approach:

We’ll write functions to take care of smaller tasks that we need to do in hangman, then use them to write the actual game itself.

### Define the function word_guessed(). 
`word_guessed()` will return True if the player has successfully guessed the word, and False otherwise.

Example:

- If the letters guessed variable has the value [’a’,’l’,’m’,’c’,’e’,’t’,’r’,’p’,’n’] word_guessed() will return True. 
- If the letters guessed variable has the value [’e’,’l’,’q’,’t’,’r’,’p’,’n’] word_guessed() will return False.
  - Hint: Obviously, you’ll use a loop. There are two things you could loop over – the letters in secret_word or the letters in letters_guessed. Which one do you want to loop over? Don’t just guess here, think! One of them makes sense and will be a lot easier than the other.

You’ll want to use the string library. Note how we have added the line from string import * to the top of the template. This imports all of the functions from the string library, so you can use them as if you’ve defined them within your own file.

### Define the function print_guessed()
`print_guessed()` that returns a string that contains the word with a dash '-' in place of letters not guessed yet.

Example:

- If the letters guessed variable has the value [], the expression print print_guessed() will print --------.
- If the letters guessed variable has the value [’a’,’p’], the expression print print_guessed() will print --ap--ap.
- If the letters guessed variable has the value [’a’,’l’,’m’,’c’,’e’,’t’,’r’,’p’,’n’], the expression print print_guessed() will print claptrap.
  - Hint: There are a lot of ways to go about this. One way is to iterate through secret word and append the character you want to print to a list. Then use the join function to change the list into a string: your last line will look something like return join(character list, ’’)

### Write the main game code. 
It helps to informally sketch out the code you want to write - this is called “pseudocode”: an outline of what you are going to code that helps to guide you when you begin writing code. 

Here’s an rough sketch of pseudocode, although you will want to expand on this:

```
continually loop:

print n guesses left

print word

get letter in lowercase

check - has letter already been guessed?

If so, what should I do?

If not, what should I do?

check - is letter in word?

If so, what should I do?

If not, what should I do?
```

Write out some pseudocode that details what you want to do. It’s a good idea to do this in comments within your code file, so you can use this as a guideline to write your code.

When your game code is finished, polish your game a bit using the following extension:
- Don't use the word “claptrap” every time! Underneath the function play hangman you should see a commented line that looks like this:
`# secret_word = get_word()`

Remove the '#' before it, and the secret word will be a new, random word each time!

## Hangman Extension - ASCII Graphics

Download [hangman_lib.py](https://github.com/kswarthout/has-hs-compsci-2019-20/blob/master/projects/hangman/hangman_lib.py) and [hangman_lib_demo.py](https://github.com/kswarthout/has-hs-compsci-2019-20/blob/master/projects/hangman/hangman_lib_demo.py). 

The first contains a set of ASCII graphics that you can use in your code; the second shows how to use the package. 
- You can insert these into your Hangman game to make it much more exciting than it was. 
  - Hint: Remember to add the line from hangman lib import * at the top of your code, just like in hangman lib demo.py. Do not copy the graphics into your code! Just use the import statement!
- Allow the user the option of guessing the full word early (perhaps by modifying your prompt to say something like, Enter a letter, or the word ’guess’ to try and guess the full word: ) Then, allow the user a try to enter in the full word) Take off 2 guesses if they enter an incorrect word…
- Modify your print guessed() function such that, in addition to what it already prints out, it prints out the letters the user has not yet guessed.
