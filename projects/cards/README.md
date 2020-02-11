# Deck Of Cards
Let's create a python program with classes to represent playing cards, decks of cards, and poker hands.

## Card Objects
There are fifty-two cards in a deck, each of which belongs to one of four suits and one of thirteen ranks. 
- The suits are Spades, Hearts, Diamonds, and Clubs (in descending order in bridge). 
- The ranks are Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, and King. 
  - Depending on the game that you are playing, an Ace may be higher than King or lower than 2.
  
### Attributes
The attributes for our `Card` class should be **rank** and **suit**, but what type should we use for these attributes? We could use strings, for example, 'Spade' or 'Queen' to represent ranks, however this would make it hard to compare cards and determine which had a higher rank.

An alternative would be to *encode* the ranks and suits. *Encode* means we are going to define a map between numbers and suits (or numbers and ranks).

For example:

Suit  | Integer Code
------|-------------
Spades|3
Hearts|2
Diamonds|1
Clubs|0

And for our ranks (obviously numeric cards map to their numeric value):

Rank  | Integer Code
------|-------------
Jack|11
Queen|12
King|13

## Exercises
Follow the instructions below (in-order) to create a playing card program.

### Implement Classes
1. Follow the instructions in [card.md](card.md) to implement the `Card` class
2. Follow the instructions in [deck.md](deck.md) to implement the `Deck` class
3. Follow the instructions in [hand.md](hand.md) to implement the `Hand` class
4. Follow the instructions in [extend_deck.md](extend_deck.md) to add additional functionality to the `Hand` class

### Implement The Program
Follow the instructions in [poker_hand.md](poker_hand.md) to implement a poker playing program.
