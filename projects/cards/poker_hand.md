# Implementing the PokerHand Class

The following are the possible hands in poker, in increasing order of value (and decreasing order of probability):

- pair: two cards with the same rank
- two pair: two pairs of cards with the same rank
- three of a kind: three cards with the same rank
- straight: five cards with ranks in sequence (aces can be high or low, so Ace-2-3-4-5 is a straight and so is 10-Jack-Queen-King-Ace, but Queen-King-Ace-2-3 is not.)
- flush: five cards with the same suit
- full house: three cards with one rank, two cards with another
- four of a kind: four cards with the same rank
- straight flush: five cards in sequence (as defined above) and with the same suit

The file [poker_hand.py](poker_hand.py) contains an incomplete implementation of a class that represents a poker hand, and some code that tests it. If you run poker_hand.py, it deals seven 7-card poker hands and checks to see if any of them contains a flush. Examine this code carefully before you go on.

## Methods
1. Add methods to poker_hand.py named has_pair, has_twopair, etc. for all the possible hands listed above that return True or False according to whether or not the hand meets the relevant criteria. Your code should work correctly for "hands" that contain any number of cards (although 5 and 7 are the most common sizes).
2. Write a method named classify that figures out the highest-value classification for a hand and sets the label attribute accordingly. For example, a 7-card hand might contain a flush and a pair; it should be labeled “flush”.
3. When you are convinced that your classification methods are working, the next step is to estimate the probabilities of the various hands. Write a function in poker_hand.py that shuffles a deck of cards, divides it into hands, classifies the hands, and counts the number of times various classifications appear.
4. Print a table of the classifications and their probabilities. Run your program with larger and larger numbers of hands until the output values converge to a reasonable degree of accuracy. Compare your results to the values at http://en.wikipedia.org/wiki/Hand_rankings.
