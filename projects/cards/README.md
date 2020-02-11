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

### Create a Card class

#### Decleration
The class properties `suit` and `rank` should be passed as arguments to the `__init__` method with default values `suit=0, rank=2`. A `Card` object can be instantiated using `queen_of_diamonds = Card(1, 12)`

#### Methods
- Add a `__str__` method that allows us to print a `Card` object in a way people can easily read
  - We can do this by adding *suit_names* and *rank_names* **class attributes** to the `Card` class that contain the string representation of a card's suit and rank. 
  - We can access the appropriate string by indexing into the list using the encoded values
  - To define **suit_names** use `suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']`
  - To define **rank_names** use `rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']`
  - *Note: The first element of rank_names is None because there is no card with rank zero. By including None as a place-keeper, we get a mapping with the nice property that the index 2 maps to the string '2', and so on.*
- Add a `__lt__` method to compare `Card` objects
  - `__lt__` takes two parameters, self and other, and **returns True if self is less than other**. 
  - To make your comparison you'll need to consider both suit and rank. This can change depending on the game you are playing, so we'll make the arbitrary choice that suit is more important, so for example, all of the Spades outrank all of the Diamonds, and so on. This means you'll need to make comparisons in the following order:
  ```
  # Check Suits
  if self's suit is greater than other's suit: return False
  if self's suit is less than other's suit: return True
  
  # If Suits are the same, check ranks
  if self's rank is greater than other's rank: return False
  if self's rank is less than other's rank: return True
  
  # If ranks are the same
  return False
  ```
  
### Create a Deck class
Since a deck is made up of cards, it is natural for each Deck to contain a list of cards as an attribute.

#### Decleration
The class property `cards` should be initialized inside the `__init__` method as a list of `Card` objects representing all suits and ranks. You can use a nested for loop to achieve this task.

#### Methods
- Define a `__str__` method
  - You'll want to build a return string where each card is printed to a new line (*hint*: use `\n`). This can be achieved using a for loop to iterate self.cards
  - We want the result of the `__str__` method to look as follows:
  ```
  10 of Spades
  Jack of Spades
  Queen of Spades
  King of Spades
  ```
- Define an `add_card` method
  - To add a card, we can use the list method [`append`](https://www.w3schools.com/python/ref_list_append.asp)
- Define a `pop_card` method
  - To deal cards, we would like a method that removes a card from the deck and returns it.
  - This can be achieved using the list method [`pop`](https://www.w3schools.com/python/ref_list_pop.asp)
- Define a `shuffle` method
  - We can use the function `shuffle` from the random module (*hint*: you'll need to use an import statement)
- Define a `sort` method
  - We can use the list method [`sort`](https://www.w3schools.com/python/ref_list_sort.asp) to achieve this.
  
### Create a Hand class
A "hand" is a set of cards held by one player. A hand is similar to a deck: both are made up of a set of cards, and both require operations like adding and removing cards. A hand is also different from a deck; there are operations we want for hands that don’t make sense for a deck. For example, in poker we might compare two hands to see which one wins. In bridge, we might compute a score for a hand in order to make a bid. Because this relationship is similar, but different, we want to use inheritance in our implementation.

#### Decleration
- Declare the `Hand` class to inherit from `Deck` (i.e. `class Hand(Deck)`).
- Hand will inherit `__init__` from Deck, but it doesn't really do what we want.
  - Instead of populating the hand with 52 new cards, the `__init__` method for Hand should initialize cards with an empty list.
  - By providing our own `__init__` method in `Hand`, we'll **override** the inherited method
  - Add an additional attribute `label`. This attribute should be passed as an argument (i.e. label=''), and then assigned to self
 
 #### Methods
 
### Add More Behavior to Deck

#### Define a `move_cards` method

In some games, cards are moved from one hand to another, or from a hand back to the deck. You can use move_cards for any of these operations: self can be either a Deck or a Hand, and hand, despite the name, can also be a Deck.
- move_cards takes two arguments, a `Hand` object and the number of cards to deal.
- inside the method, you should use a loop where on each iteration you add a card to self.card from the `Hand` object
- Because this method could be used by either Hands or Decks, we want to define it in the Deck class, and then inherit the behavior.

#### Define a `deal_hands ` method
- deal_hands takes two parameters, the number of hands and the number of cards per hand, and that creates new Hand objects, deals the appropriate number of cards per hand, and returns a list of Hand objects.
