# Create a Hand Class
A "hand" is a set of cards held by one player. A hand is similar to a deck: both are made up of a set of cards, and both require operations like adding and removing cards. A hand is also different from a deck; there are operations we want for hands that don’t make sense for a deck. For example, in poker we might compare two hands to see which one wins. In bridge, we might compute a score for a hand in order to make a bid. Because this relationship is similar, but different, we want to use inheritance in our implementation.

## Decleration
- Declare the `Hand` class to inherit from `Deck` (i.e. `class Hand(Deck)`).
- Hand will inherit `__init__` from Deck, but it doesn't really do what we want.
  - Instead of populating the hand with 52 new cards, the `__init__` method for Hand should initialize cards with an empty list.
  - By providing our own `__init__` method in `Hand`, we'll **override** the inherited method

## Attributes
- Add an additional attribute `label`. 
- This attribute should be passed as an argument (i.e. label=''), and then assigned to self
 
 ## Methods
 We'll leave the implementation as is for now.
 
